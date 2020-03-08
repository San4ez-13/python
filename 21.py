from random import shuffle

koloda = [2,3,4,5,6,7,8,9,10,10,10,10,11]*4
shuffle(koloda)

your_points = 0
computer_points = 0
min_computer_point = 17
move = 1
more = 'да'

while more == 'да':

    computer_card = koloda.pop()
    computer_points += computer_card

    if move == 1:
        your_cards = []
        for i in range(2):
            your_card = koloda.pop()
            your_cards.append(your_card)
            your_points += your_card
    else:
        your_card = koloda.pop()
        your_points += your_card
    print(f'''
    ==============
    ОЧКИ:
    Компьютер: {computer_points}
    Вы: {your_points}
    ==============
''')
    if move == 1:
        print(f'Вам выпали карты: {your_cards[0]} и {your_cards[1]}')
    else:
        print(f'Вам выпала карта: {your_card}')
    if your_points == computer_points:
        print('Ничья!')
        break
    elif your_points == 21 or computer_points == 21:
        if your_points == 21:
            print('Ты выиграл!')
        else:
            print('Выиграл компьютер...')
        break
    more = input('Ещё? Да или нет.\n')    
    move += 1

else:
    while computer_points < min_computer_point:
        computer_card = koloda.pop()
        computer_points += computer_card

        print(f'''
        ==============
        ОЧКИ:
        Компьютер: {computer_points}
        Вы: {your_points}
        ==============
    ''')




