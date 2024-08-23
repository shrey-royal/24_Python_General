def get_net_price(price, tax_rate, discount=0):
    return price * (1 + tax_rate) * (1 - discount)

def get_tax(price, tax_rate=0):
    return price * tax_rate