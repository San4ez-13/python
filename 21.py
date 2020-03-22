from random import shuffle


#функция возвращает перемешанную колоду
def get_deck():
    deck = []

    for suit in ('черви','пики','бубны','трефы'):
        for card in range(2,11):
            deck.append(f'{card} {suit}')
        for card in ('валет', 'дама', 'король', 'туз'):
            deck.append(f'{card} {suit}')
    shuffle(deck)
    return deck


#функция возвращает определённое количество очков для карты
def get_card_points(given_card):
    card_name = given_card.split()

    card_points = {}
    for card in range(2,11):
        card_points[f'{card}'] = card
    for card in ('валет', 'дама', 'король'):
        card_points[f'{card}'] = 10
    if card_name[0] == 'туз':
        points = input('туз 1 или 11?\n')
    else:
        points = card_points[card_name[0]]


    return points

deck = get_deck()

your_points = 0
computer_points = 0
min_computer_point = 17
move = 1
more = 'да'

while more == 'да':

    computer_card = deck.pop()
    computer_points += get_card_points(computer_card)

    if move == 1:
        your_cards = []
        for i in range(2):
            your_card = deck.pop()
            your_cards.append(your_card)
            your_points += get_card_points(your_card)
    else:
        your_card = deck.pop()
        your_points += get_card_points(your_card)

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
        computer_card = deck.pop()
        computer_points += computer_card

        print(f'''
        ==============
        ОЧКИ:
        Компьютер: {computer_points}
        Вы: {your_points}
        ==============
    ''')




