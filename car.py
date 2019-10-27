print('Введите команду:')
command = input()
engine_status = ''


while command:

    while command not in {'help', 'on', 'off', 'exit'}:
        print('Такой команды не сущетсвует')
        command = input()

    if command == 'help':
        print('''on - завожу двигатель
off - глушу двигатель
exit - выйти''')
    if command == 'on':
        if engine_status:
            print('Двигатель уже заведён')
        else:
            print('Завожу двигатель')
            engine_status = True
    if command == 'off':
        if engine_status:
            print('Глушу двигатель')
            engine_status = False
        else:
            print('Двигатель уже заглушён')


    if command == 'exit':
        print('Выхожу из машины')
        break


    print('Введите команду:')
    command = input()
