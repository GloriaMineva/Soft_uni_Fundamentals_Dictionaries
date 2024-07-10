students_dict = {}
students_lst = []
course = ''
while True:
    user_data = input()
    if ':' not in user_data:
        course = user_data
        break
    user_data = user_data.split(':')
    students_lst.append(user_data)

course = course.replace('_', ' ')

for student_record in students_lst:
    if course in student_record:
        key = student_record[0]
        value = student_record[1]
        students_dict[key] = int(value)
[print(f'{student} - {id}') for (student, id) in students_dict.items()]

