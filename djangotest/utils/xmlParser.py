import xmltodict
from djangotest.model.menu import MenuItem


def get_attribute(name, parsedDict):
    return parsedDict[name]

class MenuParser():

    def parseMenu(self):
        with open('menu.prop', 'r') as myfile:
            data=myfile.read().replace('\n', '')
        parsed = xmltodict.parse(data)
        menus = parsed["menu"]
        menuItems = menus["menuitem"]


    def createMenuItem(self, menuDict):
        menuItem = MenuItem()
        menuItem.menuText = get_attribute("menuText", dict)
        menuItem.level = get_attribute("@level", dict)
        menuItem.module = get_attribute("module", dict)

        # menuItem = MenuItem(menuText, module, type, security, level)
        print(menuItem)

    def createMenuItemRec(self, parent, menuDict):




with open('menu.prop', 'r') as myfile:
    data=myfile.read().replace('\n', '')

# print(data)

parsed = xmltodict.parse(data)

menus = parsed["menu"]
menuItems = menus["menuitem"]

def createMenuItem(menuDict):
    menuItem = MenuItem()
    level = menuDict["@level"]
    menuText = menuDict["menutext"]
    module = menuDict["module"]
    security = menuDict["security"]
    try:
        type = menuDict["type"]
    except KeyError:
        print("keyword type is missing")

    menuItem.menuText = menuText
    menuItem.level = level

    # menuItem = MenuItem(menuText, module, type, security, level)
    print(menuItem)


for i in menuItems:
    print(i)
    createMenuItem(i)


