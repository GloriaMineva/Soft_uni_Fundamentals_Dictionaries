student_grades = {}
count_students = int(input())
for i in range(count_students):
    name = input()
    grade = float(input())
    if name not in student_grades:
        student_grades[name] = []
        student_grades[name].append(grade)
    else:
        student_grades[name].append(grade)
for key, value in student_grades.items():
    average_grade = sum(value)/len(value)
    student_grades[key] = average_grade

for name, grade in student_grades.items():
    if grade >= 4.50:
        print(f'{name} -> {grade:.2f}')