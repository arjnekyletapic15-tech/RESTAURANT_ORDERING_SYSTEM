from yes_no import ask_yes_no


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