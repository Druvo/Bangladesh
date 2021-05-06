import json
import os
from types import SimpleNamespace
from .models import DivisionList


script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in


def get_absolute_path(str):
    """[Get a absolute path of a file]

    Args:
        str ([path]): [The file location/path]

    Returns:
        [str]: [full string fromate of the a path from the os]
    """
    return os.path.join(script_dir, str)


def get_file_data(str):
    """[Get json file data]

    Args:
        str ([path]): [The file location/path]

    Returns:
        [dictionary]: [The data in the file]
    """
    data = open(get_absolute_path(str), encoding="utf8")
    respons_dict = json.load(data)
    return respons_dict


def get_divisions():
    """[Get divisions list]

    Returns:
        [dictionary]: [divisions list]
    """
    info = get_file_data(r'data\divisions.json')
    return info


def get_districts():
    """[Get districts list]

    Returns:
        [dictionary]: [districts list]
    """
    info = get_file_data(r'data/districts.json')
    return info


def get_postcodes():
    """[Get postcodes list]

    Returns:
        [dictionary]: [postcodes list]
    """
    info = get_file_data(r'data/postcodes.json')
    return info


def get_upazilas():
    """[Get upazilas list]

    Returns:
        [dictionary]: [upazilas list]
    """
    info = get_file_data(r'data/upazilas.json')
    return info
