import xmltodict

from djangotest.model.menu import MenuItem

with open('config/menu.xml', 'r') as myfile:
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






