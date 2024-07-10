materials = {'shards': 0, 'fragments': 0, 'motes': 0}
while True:
    sequence = input().split(' ')
    for i in range(1, len(sequence), 2):
        if (materials['shards'] >= 250 or
                materials['fragments'] >= 250 or
                materials['motes'] >= 250):
            break
        current_material = sequence[i].lower()
        if current_material not in materials:
            materials[current_material] = int(sequence[i - 1])
        else:
            materials[current_material] += int(sequence[i - 1])
    if (materials['shards'] >= 250 or
            materials['fragments'] >= 250 or
            materials['motes'] >= 250):
        break
if materials['shards'] >= 250:
    materials['shards'] -= 250
    print('Shadowmourne obtained!')
elif materials['fragments'] >= 250:
    materials['fragments'] -= 250
    print('Valanyr obtained!')
else:
    materials['motes'] -= 250
    print('Dragonwrath obtained!')

[print(f'{key}: {value}') for key, value in materials.items()]



