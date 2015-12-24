from django.forms import forms
import xmltodict
from djangotest.model.menu import MenuItem


def parse_menu(page):
    location = '../pages/' + page + '/menu.xml'
    with open(location, 'r') as menu_file:
        parsed = xmltodict.parse(menu_file.read())

    menus = parsed["menu"]
    menuItems = menus["menuItem"]

    parsed_menu_items = []
    for item in menuItems:
        try:
            parsed_menu_items.append(create_menu_dict(item))
        except KeyError:
            print("menu item has no label or page")

    return {"menuItems" : parsed_menu_items}


def create_menu_dict(menu_dict):
    label = menu_dict['label']
    page = menu_dict['page']
    parsed_menu_item = {"label": label, "page": page}
    return parsed_menu_item

#
# def create_menu_dict_rec(menu_dict, menu_item):
#     try:
#         sub_menu_dict = menu_dict["menuItem"]
#         menu_item["menuItem"] = create_menu_dict()
#     except KeyError:
#         try:
#             label = menu_dict['label']
#             page = menu_dict['page']
#             parsed_menu_item = {"label": label, "page": page}
#             menu_item["menuItem"] = parsed_menu_item
#             return menu_item
#         except KeyError:
#             print("no label or page")
#             return menu_item




