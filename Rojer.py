from random import randint, choice
from timeit import default_timer

print ('Привет! Меня зовут Роджер. А как тебя?')
name = input()
name = name.title()
print ('Приятно познакомиться,' + name)
print ('Давай проверим твои знания в математике.')

print ('Хорошо')

print(f'{name}, сколько примеров ты готов решить?')
questions_guantity = input()
while not questions_guantity.isdigit():
    print('Должна быть цифра!')
    questions_guantity = input()

print(f'{name}, до скольки бьудем считать?')
max_answer = input()
while not max_answer.isdigit():
    print('Должна быть цифра!')
    max_answer = input()

print('Хорошо, тогда начинаем...')


correct_answers = 0
fails = 0
spent_time = 0

for x in range(int(questions_guantity)):
    print(f'Пример {x+1}')

    number1 = randint(1, int(max_answer))
    number2 = randint(1, int(max_answer))
    sigh = choice('+-')

    if sigh == '-':
        while number1 < number2:
            number1 = randint(1, int(max_answer))
            number2 = randint(1, int(max_answer))
        correct_answer = number1 - number2

    if sigh == '+':
        while number1 + number2 > int(max_answer):
            number1 = randint(1, int(max_answer))
            number2 = randint(1, int(max_answer))
        correct_answer = number1 + number2

    print(f'Сколько будет {number1} {sigh} {number2}?')
    start = default_timer()
    answer = input('Введи ответ: \n')
    stop = default_timer()
    spent_time += round(stop - start)

    if int(answer) == correct_answer:
        print('Правильно!')
        correct_answers += 1
    else:
        print(f'Неправильно. Правильный ответ: {correct_answer}')
        fails += 1


if fails != 0:
    print(f'''
Правильных ответов: {correct_answers}
Ошибок: {fails}
Затраченное время: {spent_time}''')
else:
    print(f'Ты ответил правильно на все вопросы за: {spent_time}!')




