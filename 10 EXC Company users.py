company_id = {}
while True:
    command = input()
    if command == "End":
        break
    name, id_ = command.split(' -> ')
    if name not in company_id:
        company_id[name] = []
        if id_ not in company_id[name]:
            company_id[name].append(id_)
    else:
        if id_ not in company_id[name]:
            company_id[name].append(id_)
for key, value in company_id.items():
    print(f'{key}')
    for current_id in value:
        print(f'-- {current_id}')

