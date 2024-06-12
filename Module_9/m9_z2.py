DEFAULT_DISCOUNT = 0.05

price = 100

customer = {"name": "Dima"}
customer1 = {"name": "Boris", "discount": 0.15}


def get_discount_price_customer(price, customer):

    if len(customer) == 1:
        return price * (1 - DEFAULT_DISCOUNT)
    else:
        return price * (1 - customer["discount"])


print(get_discount_price_customer(price, customer))

print(get_discount_price_customer(price, customer))
