from time import sleep
from random import randint
def intro():
    print('''Вы находитесь в землях, заселённых драконами.
    Перед собой вы видите две пещеры.
    В одной из них дружелюбный дракон,
    который готов поделиться с вами своими сокровищами.
    Во второй - жадный и голодный дракон, который вас съест.''')

def select_cave():
    print('В какую пещеру вы войдёте? (нажмите клавишу 1 или 2)')
    selected_cave = int(input())
    return selected_cave

def check_cave(selected_cave):
    friendly_cave = randint(1, 2)
    print('''Вы приближаетесь к пещере...
    Её темнота заставляет вас дрожать от страха...
    Большой дракон выпригивает перед вами! Он раскрывает свою пасть и...''')
    if selected_cave == friendly_cave:
        print('Делится с вами своими сокровищами')
    else:
        print('Моментально вас съедает')

play_again = 'да'
while play_again == 'да':
    intro()
    sleep(2)
    check_cave(select_cave())
    print('Сыграем ещё? (да или нет)')
    play_again = input()
