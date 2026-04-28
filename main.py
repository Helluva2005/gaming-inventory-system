from inventory_manager import *
from file_manager import save_data, load_data
from reports import *
import inventory_manager


def main_menu():
    # Load saved data when program starts
    inventory_manager.products, inventory_manager.vendors, inventory_manager.purchase_orders = load_data()

    while True:
        print("\n=== Gaming Store Inventory System ===")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product by ID")
        print("4. Search Product by Name")
        print("5. View Low Stock Products")
        print("6. Create Purchase Order")
        print("7. Receive Shipment")
        print("8. View Purchase Orders")
        print("9. Full Inventory Report")
        print("10. Low Stock Report")
        print("11. Total Inventory Value")
        print("12. Open Purchase Orders")
        print("13. Received Purchase Orders")
        print("14. Save Data")
        print("15. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            search_product_by_id()
        elif choice == "4":
            search_product_by_name()
        elif choice == "5":
            display_low_stock_products()
        elif choice == "6":
            create_purchase_order()
        elif choice == "7":
            receive_shipment()
        elif choice == "8":
            view_purchase_orders()
        elif choice == "9":
            full_inventory_report()
        elif choice == "10":
            low_stock_report()
        elif choice == "11":
            total_inventory_value_report()
        elif choice == "12":
            open_purchase_orders_report()
        elif choice == "13":
            received_purchase_orders_report()
        elif choice == "14":
            save_data(
                inventory_manager.products,
                inventory_manager.vendors,
                inventory_manager.purchase_orders
            )
        elif choice == "15":
            save_data(
                inventory_manager.products,
                inventory_manager.vendors,
                inventory_manager.purchase_orders
            )
            print("Data saved. Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()