import json


def get_divisions():
    # with json load  (file)
    info = open('./json/divisions.json', encoding="utf8")
    respons = json.load(info)
    return respons


def get_districts():
    # with json load  (file)
    import json
    info = open('./json/districts.json', encoding="utf8")
    respons = json.load(info)
    return respons


def get_postcodes():
    # with json load  (file)
    info = open('./json/postcodes.json', encoding="utf8")
    respons = json.load(info)
    return respons


def get_upazilas():
    # with json load  (file)
    info = open('./json/upazilas.json', encoding="utf8")
    respons = json.load(info)
    return respons
