#Домашнее задание по теме "Форматирование строк".
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

print('В команде Мастера кода участников: %d!'% team1_num)
print('Итого сегодня в командах участников: %s и %s' % (team1_num , team2_num))
print('Команда Волшебники данных решила задач: {}!'.format(score_2))
print('Волшебники данных решили задачи за {} с!' .format(team1_time))
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}!')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = "‘Победа команды Мастера кода!’"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = "‘Победа команды Волшебники Данных!’"
else:
    result = "‘Ничья!’"
print(f'Уточненный результат битвы: {result}')
print('В среднем на каждого игрока в команде {com1} получилось по {com3} вопросов VS {com4} у {com2}'
      .format (com1 = "'Мастера кода'", com2 = "'Волшебники  данных'",
               com3 = score_1/team1_num, com4 = score_2/team2_num))#












