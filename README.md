Shopping Cart Class with methods to update the cart and get corresponding information

# create cart
```
cart = ShoppingCart()
```

# add items
```
cart.add_item("coffee", 2.343, 2)
cart.add_item("tea", 1.66)  # adds 1
cart.add_item("milk", 1.00, 3)
cart.add_items(
    {
        "tea": {"price": 2.22, "amount": 1},
        "coffee": {"price": 1.28, "amount": 2},
    }
)
print(cart)
```

# get item details
```
print(f"Coffee information: {cart.get_item('coffee')}")
print(f"Milk information: {cart.get_item('milk')}")
print(f"Tea information: {cart.get_item('tea')}")
```

# get amount
```
print(f"Cart total items: {cart.get_cart_item_quantity()}")  # 9
```

# get total value
```
print(f"Cart total value: {cart.get_cart_total_value()}")  # 15.68
```

# remove items
```
print(f"Coffee information: {cart.get_item('coffee')}")
cart.remove_item("coffee")  # removes 1
print(f"Coffee information: {cart.get_item('coffee')}")
cart.remove_item("coffee", 2)  # removes 2
print(f"Coffee information: {cart.get_item('coffee')}")

print(f"Milk information: {cart.get_item('milk')}")
cart.remove_item("milk", completely=True)  # removes item completely from basket
print(f"Milk information: {cart.get_item('milk')}")  # None
```

# change item price
```
print(f"Tea information: {cart.get_item('tea')}")
cart.change_item_price("tea", 1.28)
print(f"Tea information: {cart.get_item('tea')}")
```