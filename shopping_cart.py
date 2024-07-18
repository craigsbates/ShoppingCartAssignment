"""Shopping cart module to compile a shopping cart with items
"""


class ShoppingCart:
    """class that represents a shopping cart and items added"""

    def __init__(self) -> None:
        """
        Initialiser for the cart populated with no items

        Args:
            _items (dict): Dict containing items within the cart, each item will store
            the key as it's name, and a dictionary containing remaining item information
        """
        self._items = {}

    def __str__(self) -> str:
        contents = "\n".join("{}: {}".format(*i) for i in self._items.items())
        return f"Cart contains: \n{contents}\n"

    def add_item(self, item_name: str, item_price=0.0, amount=1):
        """
        Add an item with the given information to the cart contents.
        Will add an dict to class _items dict with the key being item's name
        and contents, item_price and amount within a dict.

        Args:
            item_name (str): Name of the item.
            item_price (float, optiona): Price of the item. Defaults to 0.0.
            amount (int, optional): Number of item to add. Defaults to 1.
        """
        item_name = item_name.lower()
        if not self._items.get(item_name):
            self._items[item_name] = {
                "price": round(item_price, 2),
                "amount": amount,
            }
        else:
            self._items[item_name]["amount"] += amount

    def add_items(self, items: dict):
        """
        Add multiple items to the cart.

        Args:
            items (dict): Dict represenation of items to add to cart
            format {item_name {cost:float, amount:int}}
        """
        for key, value in items.items():
            self.add_item(key, value.get("price"), value.get("amount"))

    def remove_item(self, item_name: str, amount=1, completely=False):
        """
        Remove the item of given name from cart should it exist.
        Can remove an amount, or all using completely flag

        Args:
            item_name (str): Name of item to remove.
            amount (int, options): Number of item to remove. Defaults to 1.
            completely (bool): Remove all items of name if True. Defaults to False.
        """
        if item_name in self._items:
            if completely or self._items[item_name]["amount"] <= amount:
                del self._items[item_name]
            else:
                self._items[item_name]["amount"] -= amount

    def get_item(self, item_name: str):
        """
        Get the information of a single item in the cart.

        Args:
            item_name (str): The name of the item to retrieve details for.

        Returns:
            dict or None: Dict containing information on the requsted item if it exists,
            else None.
        """
        return self._items.get(item_name)

    def get_cart_item_quantity(self) -> int:
        """
        Get the total item amount of the carts contents.

        Returns:
            int: Total number of items in the cart.
        """
        return sum(i.get("amount") for i in self._items.values())

    def get_cart_total_value(self) -> float:
        """
        Get the total value of the carts contents.

        Returns:
            float: Total value of the cart rounded to 2 decimal places.
        """
        return round(
            sum(i.get("price") * i.get("amount") for i in self._items.values()), 2
        )

    def change_item_price(self, item_name: str, item_price: float):
        """
        Change the price of a given item if it exists.

        Args:
            item_name (str): Name of the item to update the price for.
            item_price (float): New value to update item price to.
        """
        if item_name in self._items:
            self._items[item_name]["price"] = round(item_price, 2)
