import datetime

STORE_NAME = "ARJNE KYLE FOOD RESTAURANT"
WIDTH = 40
BULK_QTY = 5
BULK_RATE = 0.05
SENIOR_RATE = 0.20

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


def print_receipt(orders, subtotal, discount, discount_label, total):
    print("\n" + "=" * WIDTH)
    print(STORE_NAME.center(WIDTH))
    print(datetime.datetime.now().strftime("%b %d, %Y %I:%M %p").center(WIDTH))
    print("-" * WIDTH)
    for item, qty, price in orders:
        print(f"{item:<16}{qty:>3} x {price:>6.2f} = {qty*price:>7.2f}")
    print("-" * WIDTH)
    print(f"{'SUBTOTAL':<25}{subtotal:>15.2f}")
    if discount_label:
        print(f"{discount_label:<25}{-discount:>15.2f}")
    print(f"{'TOTAL':<25}{total:>15.2f}")
    print("=" * WIDTH)
    print("Thank you, come again!".center(WIDTH))
    print("=" * WIDTH + "\n")


def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print(" Invalid choices!  Please enter 'y' or 'n'.")


def get_item_and_qty(lookup):
    while True:
        raw = input("Item number: ").strip()
        if raw.isdigit() and int(raw) in lookup:
            break
        print("  Invalid item number.")
    while True:
        raw_qty = input("Quantity: ").strip()
        if raw_qty.isdigit() and int(raw_qty) > 0:
            break
        print("  Invalid quantity.")
    name, price = lookup[int(raw)]
    return name, int(raw_qty), price


def take_orders(lookup):
    orders = []
    while True:
        name, qty, price = get_item_and_qty(lookup)
        orders.append((name, qty, price))
        if not ask_yes_no("Order another item? (y/n): "):
            break
    return orders


def compute_totals(orders, is_senior):
    subtotal = 0.0
    total_qty = 0
    for item, qty, price in orders:
        subtotal += qty * price
        total_qty += qty

    if is_senior:
        discount, label = subtotal * SENIOR_RATE, "Senior/PWD Discount (20%)"
    elif total_qty >= BULK_QTY:
        discount, label = subtotal * BULK_RATE, "Discount (5%)"
    else:
        discount, label = 0.0, None

    return subtotal, discount, label, subtotal - discount