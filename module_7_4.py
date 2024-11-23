from module_7_2 import result

team1 = 'Мастера кода'
team2 = 'Волшебники данных'

team1_num = 5
team2_num = 6

# Использование %:
print('В команде %(team1)s: %(team1_num)s игроков!' % {'team1': 'Мастера кода', 'team1_num': 5})
print('В команде %s: %x игроков!' % ('Мастера кода', 5))
print('В команде %(team1)s: %(team1_num)s игроков!' % {'team1': team1, 'team1_num': team1_num})
print('В команде %s: %s игроков!' % (team1, team1_num))
print(sep='\n')
print('В команде %s: %s игроков!' % ('Волшебники данных', 6))
print('В команде %(team2)s: %(team2_num)s игроков!' % {'team2': 'Волшебники данных', 'team2_num': 6})
print('В команде %(team2)s: %(team2_num)s игроков!' % {'team2': team2, 'team2_num': team2_num})
print('В команде %s: %s игроков!' %( team2, team2_num))
print(sep='\n')
print('В командах %(team1)s и %(team2)s %(team1_num)s и %(team2_num)s игроков!' % {'team1': team1, 'team2': team2, 'team1_num': team1_num, 'team2_num': team2_num})
print(sep='\n')

# Использование format():
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
print('{} решили задач: {}'.format(team2, score2))
print('{team2} решили задачи за {team2_time} c!'.format(team2 = team2, team2_time = 18015.2))
print(sep='\n')

# Использование f-строк:
print(f'Команды решили {score1} и {score2} задач.')
print(sep='\n')

tasks_total = score1 + score2
time_total = team1_time + team2_time
time_avg = time_total/tasks_total

print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу')

print(sep='\n')

if score1 < score2 or score1 == score2 and team1_time > team2_time:
    print(f'Результат битвы победа команды {team1}!')
elif score2 < score1 or score1 == score2 and team2_time > team1_time:
    print(f'Результат битвы победа команды {team2}!')
else:
    print('Ничья')


def challenge_result():
    if score1 < score2 or score1 == score2 and team1_time > team2_time:
        result = f'Результат битвы победа команды {team1}!'
    elif score2 < score1 or score1 == score2 and team2_time > team1_time:
        result = f'Результат битвы победа команды {team2}!'
    else:
        result = f'Ничья'
    return result

print(f'{challenge_result()}')
