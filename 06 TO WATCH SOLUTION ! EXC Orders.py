orders_dict = {}
while True:
    product_data = input()
    if product_data == 'buy':
        break
    product_data = product_data.split(' ')
    product, price, quantity = product_data
    if product not in orders_dict:
        orders_dict[product] = [float(price), int(quantity)]
    else:
        orders_dict[product][0] = float(price)
        orders_dict[product][1] += int(quantity)
for key, values in orders_dict.items():
    orders_dict[key] = values[0] * values[1]
[print(f'{key} -> {value:.2f}') for key, value in orders_dict.items()]
