verified_ranking = {}
personal_ranking = {}


while True:
    current_contest = input()
    if current_contest == 'end of contests':
        break
    valid_contest, valid_pass = current_contest.split(':')
    verified_ranking[valid_contest] = valid_pass



while True:
    current_submission = input()
    if current_submission == 'end of submissions':
        break
    contest, password, user, points = current_submission.split('=>')
    points = int(points)
    if contest in verified_ranking.keys():
        if password == verified_ranking[contest]:
            if user not in personal_ranking.keys():
                personal_ranking[user] = {}
            if contest not in personal_ranking[user]:
                personal_ranking[user][contest] = 0
            if points > personal_ranking[user][contest]:
                personal_ranking[user][contest] = points

top_user = ''
top_points = 0

for current_user, results in personal_ranking.items():
    current_points = 0
    for value in results.values():
        current_points += value
    if current_points > top_points:
        top_points = current_points
        top_user = current_user
print(f'Best candidate is {top_user} with total {top_points} points.')
print('Ranking:')

personal_ranking = dict(sorted(personal_ranking.items(), key= lambda name:name[0]))


for key, value in personal_ranking.items():
    print(key)
    for course, points in value.items():
        print(f'#  {course} -> {points}')

