registered_courses = {}
while True:
    course_data = input()
    if course_data == 'end':
        break
    course, student = course_data.split(' : ')
    if course not in registered_courses:
        registered_courses[course] = []
        registered_courses[course].append(student)
    else:
        registered_courses[course].append(student)
for key, value in registered_courses.items():
    print(f'{key}: {len(value)}')
    for name in value:
        print(f'-- {name}')