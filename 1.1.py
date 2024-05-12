restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu.update({"Beverages": {"Soda": 2.99, "Beer": 4.99}})
restaurant_menu.update({"Main Course": {"Steak": 17.99, "Salmon": 13.99}})
restaurant_menu.update({"Starters": {"Soup": 5.99}})

def menu_show():
    for course, entre in restaurant_menu.items():
        print()
        print(course + ":")
        for price in entre:
            print(price + ":", entre[price])

menu_show()