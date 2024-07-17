"""Unit test suite to test shopping cart class and functionality"""
import unittest
from shopping_cart import ShoppingCart


class TestShoppingCart(unittest.TestCase):
    """Test class to test shopping cart"""

    def setUp(self) -> None:
        """Set up the base test environment"""
        self.cart = ShoppingCart()

        # add items
        self.cart.add_item("coffee", 2.343, 4)
        self.cart.add_item("tea", 1.66)  # adds 1

    def test_add_item(self):
        """Test add item all functionality"""
        self.cart.add_item("milk", 1.50)
        self.assertEqual(self.cart.get_item("milk"), {"price": 1.50, "amount": 1})
        self.cart.add_item("coffee", amount=5)
        self.assertEqual(self.cart.get_item("coffee").get("amount"), 9)

    def test_add_items(self):
        """Test adding multiple items"""
        self.cart.add_items(
            {
                "tea": {"price": 2.22, "amount": 1},
                "milk": {"price": 1.28, "amount": 2},
            }
        )
        self.assertEqual(self.cart.get_item("tea"), {"price": 1.66, "amount": 2})
        self.assertEqual(self.cart.get_item("milk"), {"price": 1.28, "amount": 2})

    def test_remove_item(self):
        """Test remove item all functionality"""
        self.cart.remove_item("coffee")
        self.assertEqual(self.cart.get_item("coffee").get("amount"), 3)
        self.cart.remove_item("coffee", 2)
        self.assertEqual(self.cart.get_item("coffee").get("amount"), 1)
        self.cart.remove_item("coffee", completely=True)
        self.assertIsNone(self.cart.get_item("coffee"))

    def test_get_item(self):
        """Test getting details of an item"""
        self.assertIsNone(self.cart.get_item("eggs"))
        self.assertEqual(self.cart.get_item("tea"), {"price": 1.66, "amount": 1})

    def test_get_cart_total_value(self):
        """Test getting the car total value"""
        self.assertEqual(self.cart.get_cart_total_value(), 11.02)

    def test_get_cart_item_amount(self):
        """Test getting the cart total item count"""
        self.assertEqual(self.cart.get_cart_item_quantity(), 5)

    def test_change_item_price(self):
        """Test changing an items price"""
        self.cart.change_item_price("coffee", 1.99)
        self.assertEqual(self.cart.get_item("coffee").get("price"), 1.99)


if __name__ == "__main__":
    unittest.main()
