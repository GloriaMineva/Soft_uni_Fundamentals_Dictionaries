countries = input().split(', ')
capitals = input().split(', ')
country_capital = dict(zip(countries, capitals))
[print(f'{key} -> {value}') for key, value in country_capital.items()]
