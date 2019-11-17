from random import randint, choice

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

for x in range(int(questions_guantity)):
    print(f'Пример {x+1}')

    number1 = randint(1, int(max_answer))
    number2 = randint(1, int(max_answer))
    sigh = choice('+-')

    if sigh == '-':
        while number1 < number2:
            number1 = randint(1, int(max_answer))
            number2 = randint(1, int(max_answer))

    if sigh == '+':
        while number1 + number2 > int(max_answer):
            number1 = randint(1, int(max_answer))
            number2 = randint(1, int(max_answer))

    print(f'Сколько будет {number1} {sigh} {number2}?')



