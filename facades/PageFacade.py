import math

page_size = 50


def get_pages_info(photos):
    photos_count = photos.__len__()
    page_count = math.ceil(photos_count / page_size) - 1

    return {
        "size": page_size,
        "photos": photos_count,
        "pages": page_count
    }


def get_pagination(page=0):
    begin = int(page) * page_size
    end = begin + page_size
    return [begin, end]
