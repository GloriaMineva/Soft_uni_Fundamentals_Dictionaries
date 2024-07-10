operations_count = int(input())
parking_register = {}


def register(name, plate_num):
    if name not in parking_register:
        parking_register[name] = plate_num
        print(f'{name} registered {plate_num} successfully')
    else:
        print(f'ERROR: already registered with plate number {plate_num}')


def unregister(name):
    if name not in parking_register:
        print(f'ERROR: user {name} not found')
    else:
        del parking_register[name]
        print(f'{name} unregistered successfully')


for i in range(operations_count):
    command = input().split(' ')
    action = command[0]
    if action == 'register':
        name = command[1]
        plate_num = command[2]
        register(name, plate_num)
    elif action == 'unregister':
        name = command[1]
        unregister(name)

for key, value in parking_register.items():
    print(f'{key} => {value}')



