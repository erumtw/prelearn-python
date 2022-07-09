from pprint import pprint
from typing import OrderedDict


menus = {
    "mocha": 50,
    "latte": 100,
    "espresso": 90,
    "green tea": 40,
    "water": 95,
}  # name: orders

# print(menus)
# print(menus.items()) 

# sorted by key
menus_sorted = sorted(menus.items(), key=lambda e: e[0])
pprint(menus_sorted)

menu_by_name = OrderedDict(menus_sorted)
pprint(menu_by_name)

[print(k,v) for k,v in menu_by_name.items()]
# sorted by value
menus_sorted2 = sorted(menus.items(), key=lambda e: e[1], reverse=True)
pprint(menus_sorted2)

menu_by_price = OrderedDict(menus_sorted2)
pprint(menu_by_price)

[print(k,v) for k,v in menu_by_price.items()]