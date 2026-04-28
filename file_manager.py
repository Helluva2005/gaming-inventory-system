import json
from models import Product, Vendor, PurchaseOrder

def save_data(products, vendors, purchase_orders, filename="inventory_data.json"):
    """
    Saves all current data (products, vendors, and purchase orders)
    into a JSON file so it can be used again later.

    Parameters:
    products (list): all product objects
    vendors (list): all vendor objects
    purchase_orders (list): all purchase order objects
    filename (str): the file where data will be saved

    Returns:
    None
    """
    data = {
        "products": [product.to_dict() for product in products],
        "vendors": [vendor.to_dict() for vendor in vendors],
        "purchase_orders": [po.to_dict() for po in purchase_orders]
    }

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    print("Data saved successfully.")

def load_data(filename="inventory_data.json"):
    """
    Loads saved data from a JSON file and recreates the objects
    so the program can continue where it left off.

    Parameters:
    filename (str): the file to load data from

    Returns:
    tuple: lists of products, vendors, and purchase orders
    """
    try:
        with open(filename, "r") as file:
            data = json.load(file)

        products = []
        for p in data["products"]:
            product = Product(
                p["product_id"],
                p["name"],
                p["category"],
                p["quantity"],
                p["reorder_level"],
                p["reorder_quantity"],
                p["unit_price"],
                p["vendor_id"]
            )
            product.active = p["active"]
            products.append(product)

        vendors = []
        for v in data["vendors"]:
            vendor = Vendor(
                v["vendor_id"],
                v["vendor_name"],
                v["contact_name"],
                v["phone"],
                v["email"],
                v["address"]
            )
            vendors.append(vendor)

        purchase_orders = []
        for po in data["purchase_orders"]:
            order = PurchaseOrder(
                po["po_number"],
                po["vendor_id"],
                po["date_created"],
                po["items_ordered"],
                po["total_cost"],
                po["status"]
            )
            purchase_orders.append(order)

        print("Data loaded successfully.")
        return products, vendors, purchase_orders

    except FileNotFoundError:
        print("No saved data found. Starting fresh.")
        return [], [], []