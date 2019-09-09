import Shoppingcart
import pytest
cart = []


def test_add_item_to_cart():
    assert Shoppingcart.add_item_to_cart(cart, 'Biscuits', 1.20, 10) ==\
           [{'item_name': 'Biscuits', 'item_price': 1.2, 'item_qty': 10}]
    assert Shoppingcart.add_item_to_cart(cart, 'Baked Beans', 0.99, 20) == \
           [{'item_name': 'Biscuits', 'item_price': 1.2, 'item_qty': 10},
            {'item_name': 'Baked Beans', 'item_price': 0.99, 'item_qty': 20}]
    assert Shoppingcart.add_item_to_cart(cart, 'Sardines', 1.89, 20) == \
           [{'item_name': 'Biscuits', 'item_price': 1.2, 'item_qty': 10},
            {'item_name': 'Baked Beans', 'item_price': 0.99, 'item_qty': 20},
            {'item_name': 'Sardines', 'item_price': 1.89, 'item_qty': 20}]


def test_get_cart_subtotal():
    assert Shoppingcart.get_cart_subtotal(cart) == 69.60
    print(cart)


def test_get_cart_items_count():
    assert Shoppingcart.get_cart_items_count(cart) == 50
