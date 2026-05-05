# Gaming Store Inventory and Purchase Order System

## Project Description
This project is a console-based inventory and purchase order system built in Python. It simulates how a small gaming store might manage its products, vendors, stock levels, and restocking process.

The program allows the user to add and manage products, track inventory levels, create purchase orders, receive shipments, and generate reports. All data is saved to a JSON file so it can be loaded again when the program is restarted.

---

## Features

- Add new products
- View all products
- Edit existing products
- Deactivate (discontinue) products
- Search products by:
  - Product ID
  - Product name
  - Category
- Sort products by:
  - Name
  - Quantity
  - Price
- View low-stock products
- Create purchase orders
- Receive shipments and update inventory
- View purchase orders
- Generate reports:
  - Full inventory report
  - Low stock report
  - Total inventory value
  - Open purchase orders
  - Received purchase orders
- Save and load data using JSON

---

## Required Files

This project includes the following files:

- `main.py` → runs the program and contains the menu system  
- `models.py` → contains the Product, Vendor, and PurchaseOrder classes  
- `inventory_manager.py` → handles core logic (add, edit, search, sort, etc.)  
- `file_manager.py` → handles saving and loading data  
- `reports.py` → contains all report functions  
- `sample_data.json` → example dataset  
- `README.md` → project documentation  
- `reflection.md` → project reflection  
- `code_explanation.txt` → explanation of key parts of the code  

---

## How to Run the Program

1. Make sure Python is installed  
2. Open the project folder in VS Code or a terminal  
3. Run the program:

```bash
python main.py