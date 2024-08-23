# import pricing as selling_price

# net_price = selling_price.get_net_price(
#     price=100,
#     tax_rate=0.28
# )

# print(net_price)
########################################################


# from pricing import get_net_price as calculate_net_price, get_tax as calculate_tax

# net_price = calculate_net_price(
#     price=1000,
#     tax_rate=0.01
# )

# print(net_price)

# print(calculate_tax(1000, 0.01))
########################################################

from pricing import *

net_price = get_net_price(
    price=100,
    tax_rate=0.1,
    discount=0.05
)

print(net_price)