from inventory_manager import *
from file_manager import save_data, load_data
from reports import *
import inventory_manager


def main_menu():
    # Load saved data when program starts
    inventory_manager.products, inventory_manager.vendors, inventory_manager.purchase_orders = load_data()

    while True:
        print("\n=== Gaming Store Inventory System ===")
        print("1. Add Vendor")
        print("2. View Vendors")
        print("3. Add Product")
        print("4. View Products")
        print("5. Sort Products by Name")
        print("6. Sort Products by Quantity")
        print("7. Sort Products by Price")
        print("8. Search Product by ID")
        print("9. Search Product by Name")
        print("10. Search Product by Category")
        print("11. View Low Stock Products")
        print("12. Edit Product")
        print("13. Deactivate Product")
        print("14. Create Purchase Order")
        print("15. Receive Shipment")
        print("16. View Purchase Orders")
        print("17. Full Inventory Report")
        print("18. Low Stock Report")
        print("19. Total Inventory Value")
        print("20. Open Purchase Orders")
        print("21. Received Purchase Orders")
        print("22. Save Data")
        print("23. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_vendor()
        elif choice == "2":
            view_vendors()
        elif choice == "3":
            add_product()
        elif choice == "4":
            view_products()
        elif choice == "5":
            sort_products_by_name()
        elif choice == "6":
            sort_products_by_quantity()
        elif choice == "7":
            sort_products_by_price()
        elif choice == "8":
            search_product_by_id()
        elif choice == "9":
            search_product_by_name()
        elif choice == "10":
            search_product_by_category()
        elif choice == "11":
            display_low_stock_products()
        elif choice == "12":
            edit_product()
        elif choice == "13":
            deactivate_product()
        elif choice == "14":
            create_purchase_order()
        elif choice == "15":
            receive_shipment()
        elif choice == "16":
            view_purchase_orders()
        elif choice == "17":
            full_inventory_report()
        elif choice == "18":
            low_stock_report()
        elif choice == "19":
            total_inventory_value_report()
        elif choice == "20":
            open_purchase_orders_report()
        elif choice == "21":
            received_purchase_orders_report()
        elif choice == "22":
            save_data(
                inventory_manager.products,
                inventory_manager.vendors,
                inventory_manager.purchase_orders
            )
        elif choice == "23":
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