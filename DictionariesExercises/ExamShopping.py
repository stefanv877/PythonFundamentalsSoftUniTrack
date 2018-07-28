"""
6. Exam Shopping
A supermarket has products which have quantities. Your task is to stock the shop before Exam Sunday. Until you
receive the command “shopping time”, add the various products to the shop’s inventory, keeping track of their
quantity (for inventory purposes). When you receive the aforementioned command, the students start pouring in
before the exam and buy various products.

The format for stocking a product is: “stock {product} {quantity}”.
The format for buying a product is: “buy {product} {quantity}”.
If a student tries to buy a product, which doesn’t exist, print “{product} doesn&#39;t exist”. If it does exist, but
it’s out of stock, print “{product} out of stock”. If a student tries buying more than the quantity of that
product, sell them all the quantity of the product (the product is left out of stock, don’t print anything).
When you receive the command “exam time”, your task is to print the remaining inventory in the following
format: “{product} -&gt; {quantity}”. If a product is out of stock, do not print it.
"""


def add_to_inventory(stock_product, stock_quantity):
    if inventory.__contains__(stock_product):
        inventory[stock_product] += stock_quantity
    else:
        inventory[stock_product] = stock_quantity


def buying_products(buy_product, buy_quantity):
    if buy_product not in inventory.keys():
        print(f"{buy_product} doesn't exist")
    elif buy_product in inventory.keys() and inventory[buy_product] == 0:
        print(f"{buy_product} out of stock")
    elif buy_product in inventory.keys() and inventory[buy_product] > 0 and inventory[buy_product] < buy_quantity:
        inventory[buy_product] = 0
    elif buy_product in inventory.keys() and inventory[buy_product] > 0 and inventory[buy_product] >= buy_quantity:
        inventory[buy_product] -= buy_quantity


def print_result():
    global product
    for product in inventory:
        if inventory[product] != 0:
            print(f"{product} -> {inventory[product]}")


inventory = {}
stock_input = input()

while stock_input != "shopping time":
    stock_input = stock_input.split(" ")
    stock_product = stock_input[1]
    stock_quantity = int(stock_input[2])

    add_to_inventory(stock_product, stock_quantity)

    stock_input = input()

buy_input = input()

while buy_input != "exam time":
    buy_input = buy_input.split(" ")
    buy_product = buy_input[1]
    buy_quantity = int(buy_input[2])

    buying_products(buy_product, buy_quantity)

    buy_input = input()

print_result()
