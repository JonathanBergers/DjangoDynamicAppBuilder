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

    print(parsed_menu_items)


def create_menu_dict(menu_dict):
    label = menu_dict['label']
    page = menu_dict['page']
    menu_item = {"label": label, "page": page}
    try:
        sub_menu_dict = menu_dict["menuItem"]
        try:
            print("SUB ITEM")
            sub_menu_item = create_menu_dict(sub_menu_dict)
            menu_item["menuItem"] = sub_menu_item
            return menu_item
        except KeyError:
            print("sub menu item has no label or page")
    except KeyError:
        print("NO SUB ITEM")
        # menu item has no sub menu
        return menu_item



parse_menu('main')
