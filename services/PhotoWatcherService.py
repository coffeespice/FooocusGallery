import cachetools.keys
from watchdog.events import FileSystemEventHandler
from facades.PhotoServiceFacade import cache_metadata, cache_photos


def clear_cache(event):
    if 'log.html' not in event.src_path:
        return

    key = cachetools.keys.hashkey(event.src_path)

    if cache_metadata.get(key) is None:
        return

    cache_metadata.pop(key)
    cache_photos.clear()


class PhotoWatcherService(FileSystemEventHandler):
    def on_modified(self, event):
        clear_cache(event)

    def on_created(self, event):
        clear_cache(event)

    def on_deleted(self, event):
        clear_cache(event)
