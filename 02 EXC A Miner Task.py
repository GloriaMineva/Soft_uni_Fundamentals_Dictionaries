resources_dct = {}
while True:
    resource = input()
    if resource == 'stop':
        break
    quantity = int(input())
    if resource not in resources_dct:
        resources_dct[resource] = quantity
    else:
        resources_dct[resource] += quantity
[print(f'{key} -> {value}') for key, value in resources_dct.items()]
