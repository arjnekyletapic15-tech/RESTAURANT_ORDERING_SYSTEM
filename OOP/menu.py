STORE_NAME = "ARJNE KYLE FOOD RESTAURANT"
WIDTH = 40

MENU = {
    "Burgers": {"Burger": 45.00, "Foot long": 100.00, "Siopao": 50.00},
    "Sides": {"French Fries": 35.00, "Hot Dog": 55.00},
    "Drinks": {"Soft Drink": 39.00, "Iced Tea": 45.00, "Bottled Water": 25.00},
}


def build_item_lookup(menu):
    lookup = {}
    number = 1
    for category in menu:
        for item in menu[category]:
            lookup[number] = (item, menu[category][item])
            number += 1
    return lookup


def display_menu(lookup):
    print("=" * WIDTH)
    print(STORE_NAME.center(WIDTH))
    print("=" * WIDTH)
    for number in lookup:
        name, price = lookup[number]
        print(f"{number:>2}. {name:<20} PHP {price:>6.2f}")
    print("=" * WIDTH)