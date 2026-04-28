from inventory_manager import products, purchase_orders


def full_inventory_report():
    """
    Shows all products currently in the inventory.
    """
    print("\n=== Full Inventory Report ===")

    if len(products) == 0:
        print("There are no products in the inventory yet.")
        return

    for product in products:
        product.display()

def low_stock_report():
    """
    Shows products that are running low and may need to be restocked.
    """
    print("\n=== Low Stock Report ===")

    found = False

    for product in products:
        if product.quantity <= product.reorder_level and product.active:
            product.display()
            found = True

    if not found:
        print("All products are currently well stocked.")

def total_inventory_value_report():
    """
    Calculates and shows the total value of all products in inventory.
    """
    print("\n=== Total Inventory Value Report ===")

    total_value = 0

    for product in products:
        if product.active:
            total_value += product.quantity * product.unit_price

    print(f"Total inventory value: ${total_value:.2f}")

def open_purchase_orders_report():
    """
    Shows all purchase orders that haven't been received yet.
    """
    print("\n=== Open Purchase Orders ===")

    found = False

    for po in purchase_orders:
        if po.status == "OPEN":
            po.display()
            found = True

    if not found:
        print("No open purchase orders right now.")

def received_purchase_orders_report():
    """
    Shows all purchase orders that have already been received.
    """
    print("\n=== Received Purchase Orders ===")

    found = False

    for po in purchase_orders:
        if po.status == "RECEIVED":
            po.display()
            found = True

    if not found:
        print("No purchase orders have been received yet.")