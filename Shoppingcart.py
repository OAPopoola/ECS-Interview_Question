# represent the shopping cart as a list and the cart items as a dictionary
# could be converted to classes down the line
cart = []
# need a catalogue for testing
# this would normally be a lookup from a database based on some item_id

store_catalogue = [{'item_name': 'Baked Beans', 'item_price': 0.99, 'itemdiscount': 15, 'bogofdiscountstring': '2 1'},
                   {'item_name': 'Biscuits', 'item_price': 1.20, 'itemdiscount': 4, 'bogofdiscountstring': '1 1'},
                   {'item_name': 'Sardines', 'item_price': 1.89, 'itemdiscount': 10, 'bogofdiscountstring': '4 1'},
                   {'item_name': 'Shampoo (Small)', 'item_price': 2.00, 'itemdiscount': 0, 'bogofdiscountstring': '3 2'},
                   {'item_name': 'Shampoo (Medium)', 'item_price': 2.00, 'itemdiscount': 0, 'bogofdiscountstring': '2 1'},
                   {'item_name': 'Shampoo (Large)', 'item_price': 1.89, 'itemdiscount': 0, 'bogofdiscountstring': '1 1'}]

# item would be specifies so {'item_name':name, 'item_price':price, 'item_qty':qty}


def add_item_to_cart(the_cart: list, name: str, price: float, qty: int) -> list:
    """This function adds the item to the cart"""
    if qty < 1:
        # to put an item in the cart it must have a quantity greater than 0
        raise Exception("Quantity must be greater than 0")

    # create the item dict
    item = {'item_name': name, 'item_price': price, 'item_qty': qty}
    print('Adding: ', item)
    if len(the_cart) == 0:
        # straight insert with no care in the world
        the_cart.append(item)
    else:
        # check to see if there is already something in the cart
        # check to see if the item is already in the basket
        for cart_item in the_cart:
            if cart_item['item_name'] == name:
                # already in cart so just do an update
                the_cart = update_cart(the_cart, name, qty + cart_item['item_qty'])
        else:
            # not already in cart
            the_cart.append(item)
    return the_cart


def get_cart_subtotal(the_cart: list) -> float:
    """This function return the raw value of the items in the cart.
    It loops through the contents of the cart and multiplies the price by the quantity"""
    carttotal = 0.00
    carttotal = sum([item['item_qty'] * item['item_price'] for item in the_cart])
    # for item in the_cart:
    #     carttotal += item['item_qty'] * item['item_price']
    # return the cart total 0 if there are no items in the cart
    return round(carttotal, 2)


def get_cart_discount(the_cart: list) -> float:
    """This function runs through the cart contents and calculates and returns the discount
     Discounts are specified in 2 ways:-
     (1) Discount as a percentage i.e 25%
     (2) Discount as buy x get 1 free
     This function should make allowance for both types
     """
    totaldiscount = 0.00
    for item in the_cart:
        # lookup whether there is a standard discount on the item
        disc = lookup_item_discount(item['item_name'])
        totaldiscount += (disc/100) * item['item_qty'] * item['item_price']
    # get the second type of discount
    # This is the bogof type. For the purposes of this exercise we will assume
    # the offer is specified as a string of 2 numbers
    for item in the_cart:
        # lookup bogof offer
        offerstr = lookup_item_bogof_discount(item['item_name'])
        if len(offerstr) != 0:
            # means it is on an offer of some sort
            offer = offerstr.split()
            # we now have the offer
            b = int(offer[0])
            f = int(offer[1])
            if item['item_qty'] > (b + f):
                # offer applies. we now need to calculate the discount to apply
                st = int(item['item_qty'] / (b + f))
                totaldiscount += (item['item_price'] * st * f)

    return round(totaldiscount, 2)


def delete_from_cart(the_cart: list, item_name: str) -> list:

    """this function deletes the item from the cart"""
    print('Removing: {} from cart'.format(item_name))
    if len(cart) > 0:
        # something is in the cart
        for item in the_cart:
            if item['item_name'] == item_name:
                # item exists in the cart
                the_cart.remove(item)
    # return the altered cart
    return the_cart


def update_cart(the_cart: list, uitem: str, newqty: int) -> list:
    """This function updates the cart item of the given item
        it replaces the current quantity with the new one passed in"""
    print('Updating: {} quantity in cart to {}'.format(uitem, newqty))
    if newqty < 1:
        raise Exception("Quantity must be greater than 0")
    for item in the_cart:
        if item['item_name'] == uitem:
            # the item is in the cart
            item['item_qty'] = newqty
    return the_cart


def lookup_item_discount(name: str) -> int:
    """This function returns the discount associated with an item in the shops catalogue"""
    for item in store_catalogue:
        if item['item_name'] == name:
            return item['itemdiscount']


def lookup_item_bogof_discount(name: str) -> str:
    """This function returns the bogof discount string associated with the item in the shop catalog"""
    for item in store_catalogue:
        if item['item_name'] == name:
            return item['bogofdiscountstring']


def print_cart_contents(the_cart: list):
    """Function prints out the contents of the cart -- used for debugging"""
    print("Cart's Contents\nITEM     PRICE    QUANTITY")
    for item in the_cart:
        print("{}  {:.2f}  {}".format(item['item_name'], item['item_price'], item['item_qty']))


def print_cart_summary(the_cart):
    print_cart_contents(the_cart)
    cart_subtotal = get_cart_subtotal(the_cart)
    cart_discount = get_cart_discount(the_cart)
    print('SubTotal: £{:.2f}'.format(cart_subtotal))
    print('Discount: £{:.2f}'.format(cart_discount))
    print('Amount Due: £{:.2f}'.format(cart_subtotal - cart_discount))
    print('Item Count: {}'.format(get_cart_items_count(the_cart)))


def get_cart_items_count(the_cart: list) -> int:
    return (sum([item['item_qty'] for item in the_cart]))


# -------------Preliminary testing - will need proper pytests-------------------------------


cart = add_item_to_cart(cart, 'Shampoo (Small)', 2.00, 50)
cart = add_item_to_cart(cart, 'Shampoo (Medium)', 2.00, 50)
cart = add_item_to_cart(cart, 'Baked Beans', 0.99, 50)
cart = add_item_to_cart(cart, 'Shampoo (Large)', 1.89, 50)
cart = add_item_to_cart(cart, 'Biscuits', 1.20, 50)
cart = add_item_to_cart(cart, 'Sardines', 1.89, 50)
cart = add_item_to_cart(cart, 'Shampoo (Small)', 2.00, 50)
print_cart_summary(cart)
cart = delete_from_cart(cart, 'Baked Beans')
print_cart_summary(cart)


