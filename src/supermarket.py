prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

# what does our inventory look like
for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]

# how much do we make if we sell everything
for food in prices:
    money = prices[food] * stock[food]
    print money
    total += money
print total

# how much would it cost to purchase our shopping list
# check stock before purchase and update stock after purchase
def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1
    return total
