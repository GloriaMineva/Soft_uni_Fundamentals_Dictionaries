contest = {}
submissions = {}
while True:
    users_data = input()
    if users_data == 'exam finished':
        break
    users_data = users_data.split('-')
    if users_data[1] == 'banned':
        name = users_data[0]
        if name in contest:
            del contest[name]
    else:
        name, language, points = users_data
        points = int(points)
        if name not in contest:
            contest[name] = 0
        if points > contest[name]:
            contest[name] = points
        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1
print('Results:')
[print(f'{name} | {points}') for name, points in contest.items()]
print('Submissions:')
[print(f'{key} - {value}') for key, value in submissions.items()]