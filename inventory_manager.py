# inventory_manager.py

from models import Product, Vendor, PurchaseOrder

products = []
vendors = []
purchase_orders = []


def add_vendor():
    """
    Adds a new vendor.
    """
    vendor_id = input("Enter vendor ID: ")

    for vendor in vendors:
        if vendor.vendor_id == vendor_id:
            print("Vendor already exists.")
            return

    vendor_name = input("Enter vendor name: ")
    contact_name = input("Enter contact name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    new_vendor = Vendor(vendor_id, vendor_name, contact_name, phone, email, address)
    vendors.append(new_vendor)

    print("Vendor added successfully.")


def view_vendors():
    """
    Displays all vendors.
    """
    if not vendors:
        print("No vendors available.")
        return

    for vendor in vendors:
        vendor.display()


def add_product():
    """
    Adds a new product to the inventory.
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
        print("Error: Values must be numbers.")
        return

    vendor_id = input("Enter vendor ID: ")

    new_product = Product(
        product_id,
        name,
        category,
        quantity,
        reorder_level,
        reorder_quantity,
        unit_price,
        vendor_id
    )

    products.append(new_product)
    print("Product added successfully.")


def view_products():
    """
    Displays all products.
    """
    if not products:
        print("No products in inventory.")
        return

    for product in products:
        product.display()


def sort_products_by_name():
    """
    Displays products sorted alphabetically by name.
    """
    if not products:
        print("No products to sort.")
        return

    sorted_list = sorted(products, key=lambda product: product.name.lower())

    for product in sorted_list:
        product.display()


def sort_products_by_quantity():
    """
    Displays products sorted by quantity in stock.
    """
    if not products:
        print("No products to sort.")
        return

    sorted_list = sorted(products, key=lambda product: product.quantity)

    for product in sorted_list:
        product.display()


def sort_products_by_price():
    """
    Displays products sorted by unit price.
    """
    if not products:
        print("No products to sort.")
        return

    sorted_list = sorted(products, key=lambda product: product.unit_price)

    for product in sorted_list:
        product.display()


def search_product_by_id():
    """
    Searches for a product by ID.
    """
    search_id = input("Enter product ID: ")

    for product in products:
        if product.product_id == search_id:
            product.display()
            return

    print("Product not found.")


def search_product_by_name():
    """
    Searches for products by name.
    """
    search_name = input("Enter product name: ").lower()

    found = False

    for product in products:
        if search_name in product.name.lower():
            product.display()
            found = True

    if not found:
        print("No matching products found.")


def search_product_by_category():
    """
    Searches for products by category.
    """
    search_category = input("Enter category to search: ").lower()

    found = False

    for product in products:
        if search_category in product.category.lower():
            product.display()
            found = True

    if not found:
        print("No products found in that category.")


def display_low_stock_products():
    """
    Displays products that need restocking.
    """
    found = False

    for product in products:
        if product.quantity <= product.reorder_level and product.active:
            product.display()
            found = True

    if not found:
        print("No low-stock products found.")


def edit_product():
    """
    Allows the user to update an existing product's information.
    """
    product_id = input("Enter product ID to edit: ")

    for product in products:
        if product.product_id == product_id:
            print("Leave a field blank to keep current value.\n")

            new_name = input(f"Enter new name ({product.name}): ")
            if new_name:
                product.name = new_name

            new_category = input(f"Enter new category ({product.category}): ")
            if new_category:
                product.category = new_category

            try:
                new_quantity = input(f"Enter new quantity ({product.quantity}): ")
                if new_quantity:
                    product.quantity = int(new_quantity)

                new_reorder_level = input(f"Enter new reorder level ({product.reorder_level}): ")
                if new_reorder_level:
                    product.reorder_level = int(new_reorder_level)

                new_reorder_quantity = input(f"Enter new reorder quantity ({product.reorder_quantity}): ")
                if new_reorder_quantity:
                    product.reorder_quantity = int(new_reorder_quantity)

                new_price = input(f"Enter new unit price ({product.unit_price}): ")
                if new_price:
                    product.unit_price = float(new_price)

            except ValueError:
                print("Invalid number entered. Update cancelled.")
                return

            print("Product updated successfully.")
            return

    print("Product not found.")


def deactivate_product():
    """
    Marks a product as discontinued instead of deleting it.
    """
    product_id = input("Enter product ID to deactivate: ")

    for product in products:
        if product.product_id == product_id:
            product.active = False
            print("Product has been marked as discontinued.")
            return

    print("Product not found.")


def create_purchase_order():
    """
    Creates a purchase order.
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
        product_id = input("Enter product ID (or 'done' to finish): ")

        if product_id.lower() == "done":
            break

        try:
            quantity = int(input("Enter quantity: "))
            unit_price = float(input("Enter unit price: "))
        except ValueError:
            print("Quantity and unit price must be numbers.")
            return

        item = {
            "product_id": product_id,
            "quantity": quantity,
            "unit_price": unit_price
        }

        items_ordered.append(item)
        total_cost += quantity * unit_price

    if not items_ordered:
        print("No items added.")
        return

    new_po = PurchaseOrder(
        po_number,
        vendor_id,
        date_created,
        items_ordered,
        total_cost,
        "OPEN"
    )

    purchase_orders.append(new_po)
    print("Purchase order created.")


def receive_shipment():
    """
    Receives a purchase order and updates inventory.
    """
    po_number = input("Enter PO number: ")

    for po in purchase_orders:
        if po.po_number == po_number:
            if po.status == "RECEIVED":
                print("Already received.")
                return

            for item in po.items_ordered:
                for product in products:
                    if product.product_id == item["product_id"]:
                        product.quantity += item["quantity"]

            po.status = "RECEIVED"
            print("Shipment received.")
            return

    print("Purchase order not found.")


def view_purchase_orders():
    """
    Displays all purchase orders.
    """
    if not purchase_orders:
        print("No purchase orders.")
        return

    for po in purchase_orders:
        po.display()