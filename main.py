import cherrypy
import os
import json
from services.PhotoService import list_photos, list_metadatas, search
from services.ConfigService import load_env, outputs_directory
from apscheduler.schedulers.background import BackgroundScheduler
from watchdog.observers import Observer
from services.PhotoWatcherService import PhotoWatcherService
from services.FooocusService import regenerate, vary_upscale


class Root(object):
    @cherrypy.expose
    def index(self):
        return open('static/index.html')

    @cherrypy.expose
    def public(self):
        return open('public')

    @cherrypy.expose
    def photos(self, page):
        page_size = 50
        begin = int(page) * page_size
        end = begin + page_size
        photos = list_photos(begin, end)
        return json.dumps(photos)

    @cherrypy.expose
    def metadatas(self, dirs=None):
        directories = dirs.split(',') if dirs is not None else None
        return json.dumps(list_metadatas(directories))

    @cherrypy.expose
    def search(self, page, prompt):
        page_size = 50
        begin = int(page) * page_size
        end = begin + page_size
        prompts = prompt.lower().split(',')
        dtos = search(prompts, begin, end)
        return json.dumps(dtos)

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def regenerate(self):
        prompt = cherrypy.request.json
        regenerate(prompt)
        return json.dumps([])

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def vary_subtle(self):
        data = cherrypy.request.json
        data["prompt"] = json.loads(data.get('prompt'))
        data["action"] = "Vary (Subtle)"
        vary_upscale(**data)
        return json.dumps([])

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def vary_strong(self):
        data = cherrypy.request.json
        data["prompt"] = json.loads(data.get('prompt'))
        data["action"] = "Vary (Strong)"
        vary_upscale(**data)
        return json.dumps([])

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def upscale_150(self):
        data = cherrypy.request.json
        data["prompt"] = json.loads(data.get('prompt'))
        data["action"] = "Upscale (1.5x)"
        vary_upscale(**data)
        return json.dumps([])

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def upscale_200(self):
        data = cherrypy.request.json
        data["prompt"] = json.loads(data.get('prompt'))
        data["action"] = "Upscale (2x)"
        vary_upscale(**data)
        return json.dumps([])


if __name__ == '__main__':
    load_env()

    conf = {
        'global': {
            'engine.autoreload.on': False
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.abspath('static'),
        },
        '/outputs': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': outputs_directory(),
        }
    }

    scheduler = BackgroundScheduler()
    scheduler.add_job(list_metadatas, 'interval', minutes=1, max_instances=1)
    scheduler.start()

    observer = Observer()
    observer.schedule(PhotoWatcherService(), path=outputs_directory(), recursive=True)
    observer.start()

    cherrypy.server.socket_host = '0.0.0.0'
    cherrypy.quickstart(Root(), '/', conf)
