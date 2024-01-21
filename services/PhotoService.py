import concurrent.futures
import os

from facades.PageFacade import get_pages_info
from facades.PhotoServiceFacade import get_metadata, list_all_photos, make_photo_dtos
from services.ConfigService import outputs_directory


def list_photos(begin, end):
    [photos, outputs] = list_all_photos()
    paginated = photos[begin:end]
    pages_info = get_pages_info(photos)

    if paginated.__len__() == 0:
        return [[], pages_info]

    outputs = list(set(outputs[begin:end]))
    metadatas = list_metadatas(outputs)
    dtos = make_photo_dtos(paginated, metadatas)
    return [dtos, pages_info]


def list_metadatas(directories=None):
    directories = directories or os.listdir(outputs_directory())
    metadatas = {}

    with concurrent.futures.ThreadPoolExecutor() as executor:
        paths = [os.path.join(outputs_directory(), directory, 'log.html') for directory in directories]
        paths = [path for path in paths if os.path.exists(path)]
        results = executor.map(get_metadata, paths)

        for metadata in results:
            metadatas.update(metadata)

    return metadatas


def search(prompts, begin, end):
    [photos, _] = list_all_photos()
    metadatas = list_metadatas()
    dtos = make_photo_dtos(photos, metadatas)
    filtered = [dto for dto in dtos if any(p in (dto.get('prompt') or '').lower() for p in prompts)]
    return [filtered[begin:end], get_pages_info(filtered)]
