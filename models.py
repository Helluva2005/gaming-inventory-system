class Product:
    """
    Represents a gaming product in the inventory system.
    """

    def __init__(self, product_id, name, category, quantity, reorder_level, reorder_quantity, unit_price, vendor_id):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.reorder_level = reorder_level
        self.reorder_quantity = reorder_quantity
        self.unit_price = unit_price
        self.vendor_id = vendor_id
        self.active = True

    def to_dict(self):
        """
        Converts the product object to a dictionary for saving to JSON.
        """
        return {
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category,
            "quantity": self.quantity,
            "reorder_level": self.reorder_level,
            "reorder_quantity": self.reorder_quantity,
            "unit_price": self.unit_price,
            "vendor_id": self.vendor_id,
            "active": self.active
        }

    def display(self):
        """
        Displays product information in a readable format.
        """
        status = "Available" if self.active else "Discontinued"
        print(f"ID: {self.product_id} | Name: {self.name} | Category: {self.category}")
        print(f"Stock: {self.quantity} | Reorder Level: {self.reorder_level}")
        print(f"Price: ${self.unit_price:.2f} | Vendor ID: {self.vendor_id} | Status: {status}")
        print("-" * 50)

class Vendor:
    """
    Represents a vendor that supplies gaming products.
    """

    def __init__(self, vendor_id, vendor_name, contact_name, phone, email, address):
        self.vendor_id = vendor_id
        self.vendor_name = vendor_name
        self.contact_name = contact_name
        self.phone = phone
        self.email = email
        self.address = address

    def to_dict(self):
        """
        Converts the vendor object to a dictionary for saving to JSON.
        """
        return {
            "vendor_id": self.vendor_id,
            "vendor_name": self.vendor_name,
            "contact_name": self.contact_name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address
        }

    def display(self):
        """
        Displays vendor information in a readable format.
        """
        print(f"Vendor ID: {self.vendor_id}")
        print(f"Name: {self.vendor_name}")
        print(f"Contact: {self.contact_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")
        print(f"Address: {self.address}")
        print("-" * 50)

class PurchaseOrder:
    """
    Represents a purchase order for restocking gaming inventory.
    """

    def __init__(self, po_number, vendor_id, date_created, items_ordered, total_cost, status):
        self.po_number = po_number
        self.vendor_id = vendor_id
        self.date_created = date_created
        self.items_ordered = items_ordered
        self.total_cost = total_cost
        self.status = status

    def to_dict(self):
        """
        Converts the purchase order object to a dictionary for saving to JSON.
        """
        return {
            "po_number": self.po_number,
            "vendor_id": self.vendor_id,
            "date_created": self.date_created,
            "items_ordered": self.items_ordered,
            "total_cost": self.total_cost,
            "status": self.status
        }

    def display(self):
        """
        Displays purchase order information in a readable format.
        """
        print(f"PO Number: {self.po_number}")
        print(f"Vendor ID: {self.vendor_id}")
        print(f"Date Created: {self.date_created}")
        print(f"Status: {self.status}")
        print(f"Total Cost: ${self.total_cost:.2f}")
        print("Items Ordered:")

        for item in self.items_ordered:
            print(f"- Product ID: {item['product_id']} | Quantity: {item['quantity']} | Unit Price: ${item['unit_price']:.2f}")

        print("-" * 50)