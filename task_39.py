# 2. Создать программу для игры с конфетами человек против человека
# Условия задачи:
# На столе лежат конфеты. Играют два игрока, делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем установленных конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

from random import randint

candies = int(input('Сколько конфет будем разыгрывать: '))
take = int(input("Сколько конфет можно взять за один ход: "))

# Сколько конфет нужно взять, чтобы  выиграть
def take_to_have_for_first(candies, take):
    take_candies = candies % (take + 1)
    if take_candies == 0:
        take_candies = take
    return(f'Чтобы выиграть, первому ходящему необходимо взять: {take_candies} конфет')

# Определяем, кто ходит первым кто вторым
first_move = randint(1, 2)
print(f'Первым ходит игрок: {first_move}')
second_move = 3 - first_move
print(f'Вторым ходит игрок: {second_move}')

count = 0
while candies > 0:
    count += 1
    player1 = int(input("Первый ход. Сколько конфет возьмёте: "))
    candies = candies - player1 
    print(f'Осталось {candies} конфет')
    print(take_to_have_for_first(candies, take))
    if candies > 0: 
        player2 = int(input("Второй ход. Сколько конфет возьмёте: "))
        candies = candies - player2
        print(f'Осталось {candies} конфет')
        print(take_to_have_for_first(candies, take))
if candies == 0:
    if take % 2 != 0:
        print(f'Победил игрок {first_move}')
        print('Конец!')
    else:
        print(f'Победил игрок {second_move}')
        print('Конец!')