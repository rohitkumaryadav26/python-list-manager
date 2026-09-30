from utils import add_item, remove_item


def test_add_item():
    items = []

    add_item(items, "Apple")

    assert items == ["Apple"]


def test_remove_item():
    items = ["Apple", "Banana"]

    remove_item(items, "Apple")

    assert items == ["Banana"]


def test_add_multiple_items():
    items = []

    add_item(items, "Apple")
    add_item(items, "Banana")
    add_item(items, "Mango")

    assert items == ["Apple", "Banana", "Mango"]


def test_remove_item_from_list():
    items = ["Apple", "Banana", "Mango"]

    remove_item(items, "Banana")

    assert items == ["Apple", "Mango"]