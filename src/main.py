from utils import add_item, remove_item, display_items


def main():
    items = []

    while True:
        print("\n===== List Manager =====")
        print("1. Add Item")
        print("2. View List")
        print("3. Delete Item")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            item = input("Enter item to add: ").strip()

            if item:
                add_item(items, item)
                print(f"'{item}' added successfully.")
            else:
                print("Item cannot be empty.")

        elif choice == "2":
            display_items(items)

        elif choice == "3":
            item = input("Enter item to delete: ").strip()

            if remove_item(items, item):
                print(f"'{item}' deleted successfully.")
            else:
                print(f"'{item}' was not found.")

        elif choice == "4":
            print("Exiting List Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()