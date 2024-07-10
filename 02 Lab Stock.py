elements = input().split(' ')
to_search_for = input().split(' ')
menu = {}
for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    menu[key] = int(value)

for product in to_search_for:
    if product in menu:
        print(f'We have {menu[product]} of {product} left')
    else:
        print(f'Sorry, we don\'t have {product}')