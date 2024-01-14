import cherrypy
import os
import json
import asyncio
from services.PhotoService import list_photos, list_metadatas, search
from services.ConfigService import load_env, outputs_directory


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


if __name__ == '__main__':
    load_env()

    conf = {
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.abspath('static'),
        },
        '/outputs': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': outputs_directory(),
        }
    }

    cherrypy.server.socket_host = '0.0.0.0'
    cherrypy.quickstart(Root(), '/', conf)
