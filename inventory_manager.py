from models import Product, Vendor, PurchaseOrder


products = []
vendors = []
purchase_orders = []

def add_product():
    """
    Adds a new product to the inventory.

    Parameters:
    None

    Returns:
    None
    """
    product_id = input("Enter product ID: ")

    for product in products:
        if product.product_id == product_id:
            print("Error: A product with that ID already exists.")
            return

    name = input("Enter product name: ")
    category = input("Enter category: ")

    try:
        quantity = int(input("Enter quantity in stock: "))
        reorder_level = int(input("Enter reorder level: "))
        reorder_quantity = int(input("Enter reorder quantity: "))
        unit_price = float(input("Enter unit price: "))
    except ValueError:
        print("Error: Quantity, reorder level, reorder quantity, and price must be numbers.")
        return

    vendor_id = input("Enter vendor ID: ")

    new_product = Product(product_id, name, category, quantity, reorder_level, reorder_quantity, unit_price, vendor_id)
    products.append(new_product)

    print("Product added successfully.")

def view_products():
    """
    Displays all products in the inventory.

    Parameters:
    None

    Returns:
    None
    """
    if not products:
        print("No products in inventory.")
        return

    for product in products:
        product.display()
    
def search_product_by_id():
    """
    Searches for a product by its ID and displays it.

    Parameters:
    None

    Returns:
    None
    """
    search_id = input("Enter product ID to search: ")

    for product in products:
        if product.product_id == search_id:
            product.display()
            return

    print("Product not found.")

def search_product_by_name():
    """
    Searches for products by name (partial match allowed).

    Parameters:
    None

    Returns:
    None
    """
    search_name = input("Enter product name to search: ").lower()

    found = False

    for product in products:
        if search_name in product.name.lower():
            product.display()
            found = True

    if not found:
        print("No matching products found.")

def display_low_stock_products():
    """
    Displays products where quantity is at or below the reorder level.

    Parameters:
    None

    Returns:
    None
    """
    found = False

    for product in products:
        if product.quantity <= product.reorder_level and product.active:
            product.display()
            found = True

    if not found:
        print("No low-stock products found.")

def create_purchase_order():
    """
    Creates a purchase order for restocking products.

    Parameters:
    None

    Returns:
    None
    """
    po_number = input("Enter PO number: ")

    for po in purchase_orders:
        if po.po_number == po_number:
            print("Error: Purchase order already exists.")
            return

    vendor_id = input("Enter vendor ID: ")
    date_created = input("Enter date (YYYY-MM-DD): ")

    items_ordered = []
    total_cost = 0

    while True:
        product_id = input("Enter product ID to add (or type 'done' to finish): ")

        if product_id.lower() == "done":
            break

        quantity = int(input("Enter quantity: "))
        unit_price = float(input("Enter unit price: "))

        item = {
            "product_id": product_id,
            "quantity": quantity,
            "unit_price": unit_price
        }

        items_ordered.append(item)
        total_cost += quantity * unit_price

    if not items_ordered:
        print("Error: No items added to purchase order.")
        return

    new_po = PurchaseOrder(po_number, vendor_id, date_created, items_ordered, total_cost, "OPEN")
    purchase_orders.append(new_po)

    print("Purchase order created successfully.")

def receive_shipment():
    """
    Marks a purchase order as received and updates inventory quantities.

    Parameters:
    None

    Returns:
    None
    """
    po_number = input("Enter PO number to receive: ")

    for po in purchase_orders:
        if po.po_number == po_number:
            if po.status == "RECEIVED":
                print("Error: This purchase order has already been received.")
                return

            for item in po.items_ordered:
                for product in products:
                    if product.product_id == item["product_id"]:
                        product.quantity += item["quantity"]

            po.status = "RECEIVED"
            print("Shipment received and inventory updated.")
            return

    print("Purchase order not found.")

def view_purchase_orders():
    """
    Displays all purchase orders.

    Parameters:
    None

    Returns:
    None
    """
    if not purchase_orders:
        print("No purchase orders found.")
        return

    for po in purchase_orders:
        po.display()