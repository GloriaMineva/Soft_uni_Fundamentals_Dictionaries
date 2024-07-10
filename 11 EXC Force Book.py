jedi_exists = False
side_exists = False
force = {}


while True:
    data_input = input()
    if data_input == 'Lumpawaroo':
        break
    if '|' in data_input:
        side, jedi = data_input.split(' | ')
        if side in force:
            side_exists = True
        for current_side in force.values():
            if jedi in current_side:
                jedi_exists = True
                break
        if jedi_exists is False and side_exists is False:
            force[side] = []
            force[side].append(jedi)
        elif jedi_exists is False and side_exists is True:
            force[side].append(jedi)
    elif '->' in data_input:
        jedi, side = data_input.split(' -> ')
        if side in force:
            side_exists = True
        for current_side in force.values():
            if jedi in current_side:
                jedi_exists = True
                break
        if jedi_exists is False and side_exists is False:
            force[side] = []
            force[side].append(jedi)
        elif jedi_exists is False and side_exists is True:
            force[side].append(jedi)
        elif jedi_exists is True:
            for key, value in force.items():
                for current_list in value:
                    if jedi in current_list:
                        value.remove(jedi)
            if side_exists is True:
                force[side].append(jedi)
            else:
                force[side] = []
                force[side].append(jedi)
        print(f'{jedi} joins the {side} side!')


for key, value in force.items():
    if len(value) > 0:
        print(f'Side: {key}, Members: {len(value)}')
    for current_jedi in value:
        print(f'! {current_jedi}')


