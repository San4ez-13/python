print ('Привет! Меня зовут Роджер. А как тебя?')
name = input()
name = name.title()
print ('Приятно познакомиться,' + name)
print ('''Давай проверим твои знания в математике.
Ты готов? (да или нет)''')
ready = input()
ready = ready.lower()

while ready not in {'да','нет'}:
    print('''Должно быть да или нет.
Введи заново.''')
    ready = input()
    ready = ready.lower()

if ready == 'да':
    print ('Хорошо')
else:
    print ('''Передумал? Хорошо, может как-нибудь в следующий раз...
Пока!''')
print(f'{name}, сколько примеров ты готов решить?')