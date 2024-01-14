import os
import concurrent.futures
from facades.PhotoServiceFacade import get_html_file, parse_metadata, list_all_photos, make_photo_dtos
from services.ConfigService import outputs_directory


def list_photos(begin, end):
    [photos, outputs] = list_all_photos()
    photos = photos[begin:end]

    if photos.__len__() == 0:
        return []

    outputs = list(set(outputs[begin:end]))
    metadatas = list_metadatas(outputs)
    return make_photo_dtos(photos, metadatas)


def list_metadatas(directories=None):
    directories = directories or os.listdir(outputs_directory())
    html_files = []
    metadatas = {}

    with concurrent.futures.ThreadPoolExecutor() as executor:
        paths = [os.path.join(outputs_directory(), directory, 'log.html') for directory in directories]
        results = executor.map(get_html_file, paths)

        for html_file in results:
            if html_file is not None:
                html_files.append(html_file)

    for html_file in html_files:
        metadatas.update(parse_metadata(html_file))

    return metadatas


def search(prompts, begin, end):
    [photos, _] = list_all_photos()
    metadatas = list_metadatas()
    dtos = make_photo_dtos(photos, metadatas)
    filtered = [dto for dto in dtos if any(p in (dto.get('prompt') or '').lower() for p in prompts)]
    return filtered[begin:end]
