import os
from functools import lru_cache

from bs4 import BeautifulSoup
from lxml import html
from services.ConfigService import outputs_directory
from cachetools import cached, LRUCache

cache_metadata = LRUCache(1024)
cache_photos = LRUCache(1024)


def get_html_file(path):
    try:
        with open(path, 'r') as file:
            soup = BeautifulSoup(file.read(), 'html.parser')
            return html.fromstring(str(soup))
    except FileNotFoundError:
        print('')


def parse_metadata(html_file):
    datas = {}
    for div in html_file.xpath('//div[@class="image-container"]'):
        data = {}
        key = div.get('id')

        for tr in div.xpath('.//table[@class="metadata"]/tr'):
            td_key = tr.xpath('.//td[@class="key"] | .//td[@class="label"]')[0].text.lower()
            td_value = tr.xpath('.//td[@class="value"]')[0].text

            if td_key == 'resolution':
                td_value = td_value.replace('(', '').replace(')', '').split(',')

            data[td_key] = td_value

        button = div.xpath('.//button')

        if button.__len__() > 0:
            click = button[0].get('onclick')
            data['click'] = click

        datas[key] = data

    return datas


@cached(cache_metadata)
def get_metadata(path):
    html_file = get_html_file(path)
    return parse_metadata(html_file)


@cached(cache_photos)
def list_all_photos():
    photos = []
    outputs = []

    for output in os.listdir(outputs_directory()):
        path = os.path.join(outputs_directory(), output)
        for photo in os.listdir(path):
            joined_path = os.path.join('outputs', output, photo)
            photos.append(joined_path)
            outputs.append(output)

    return [photos, outputs]


def make_photo_dtos(photos, metadatas):
    dtos = []

    for photo in photos:
        key = photo.split(os.path.sep)[2].replace('.', '_')
        dto = {'src': photo}

        if key in metadatas:
            dto.update(metadatas[key])

        dtos.append(dto)

    return dtos
