def add_item(items, item):
    """Add an item to the list."""
    items.append(item)
    return items


def remove_item(items, item):
    """Remove an item from the list if it exists."""
    if item in items:
        items.remove(item)
        return True
    return False


def display_items(items):
    """Display all items with proper formatting."""
    if not items:
        print("\nThe list is empty.")
        return

    print("\nCurrent List:")
    for index, item in enumerate(items, start=1):
        print(f"{index}. {item}")