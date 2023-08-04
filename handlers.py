from menu import Menu
from birds import Birds
from detail import Detail
from add import Add
from hashmap import HashMap
from seen import Seen


# main menu
def menu_on_start(hashMap: HashMap, _files=None, _data=None) -> HashMap:
    return Menu.on_start(hashMap, _files, _data)


def menu_on_input(hashMap: HashMap, _files=None, _data=None) -> HashMap:
    return Menu.on_input(hashMap, _files, _data)


# birds list
def birds_list_on_start(hashMap: HashMap, _files=None, _data=None) -> HashMap:
    return Birds.on_start(hashMap, _files, _data)


def birds_list_on_input(hashMap: HashMap, _files=None, _data=None) -> HashMap:
    return Birds.on_input(hashMap, _files, _data)


# add bird
def add_bird_on_start(hashMap: HashMap, _files=None, _data=None) -> HashMap:
    return Add.on_start(hashMap, _files, _data)


def add_bird_on_input(hashMap: HashMap, _files=None, _data=None) -> HashMap:
    return Add.on_input(hashMap, _files, _data)


# bird detail
def bird_detail_on_start(hashMap: HashMap, _files=None, _data=None) -> HashMap:
    return Detail.on_start(hashMap, _files, _data)


def bird_detail_on_input(hashMap: HashMap, _files=None, _data=None) -> HashMap:
    return Detail.on_input(hashMap, _files, _data)


# seen birds list
def seen_on_start(hashMap: HashMap, _files=None, _data=None) -> HashMap:
    return Seen.on_start(hashMap, _files, _data)


def seen_on_input(hashMap: HashMap, _files=None, _data=None) -> HashMap:
    return Seen.on_input(hashMap, _files, _data)
