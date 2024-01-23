import cachetools.keys
import re
from watchdog.events import FileSystemEventHandler
from facades.PhotoServiceFacade import cache_metadata, cache_photos


def clear_cache(event):
    cache_photos.clear()
    if 'log.html' not in event.src_path:
        return

    path = re.sub(r"(\.)?log\.html.*", "log.html", event.src_path)
    key = cachetools.keys.hashkey(path)

    if cache_metadata.get(key) is None:
        return

    cache_metadata.pop(key)


class PhotoWatcherService(FileSystemEventHandler):
    def on_modified(self, event):
        clear_cache(event)

    def on_created(self, event):
        clear_cache(event)

    def on_deleted(self, event):
        clear_cache(event)
