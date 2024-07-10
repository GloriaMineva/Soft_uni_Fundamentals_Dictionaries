bakery = {}
while True:
    data_input = input()
    if data_input == 'statistics':
        break
    data_input = data_input.split(': ')
    key = data_input[0]
    value = int(data_input[1])
    if key not in bakery:
        bakery[key] = value
    else:
        bakery[key] += value

print('Products in stock:')
# for product, quantity in bakery.items():
#     print(f'- {product}: {quantity}')
[print(f'- {product}: {quantity}') for (product, quantity) in bakery.items()]
print(f'Total Products: {len(bakery.items())}')
print(f'Total Quantity: {sum(bakery.values())}')