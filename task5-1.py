# Создайте программу для игры с конфетами человек против компьютера.
# Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера. Первый ход определяется жеребьёвкой.За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Подумайте как наделить бота ""интеллектом""

from random import randint as rnd
jereb=rnd(1,20)
total_qty=150
whos_move=0
if jereb%2>0:
    print("Жеребьёвкой выбран пользователь.")
    move_qty=int(input('Введите кол-во конфет для первого хода: '))
    whos_move=1
else:
    print("Жеребьёвкой выбран компьютер.")
    move_qty=total_qty%29
    print("Ходит компьютер:", move_qty)
    whos_move=2

if move_qty>28 or move_qty<1:
        print('Правила нарушены. Игра окончена')
        exit()
total_qty-=move_qty

while total_qty>0:
    if whos_move==2:
        whos_move=1
    else:
        whos_move=2

    if whos_move==1:
        move_qty = int(input('Ход игрока, введи количество хода: '))
    else:
        if total_qty%29!=0:
            move_qty=total_qty%29
        else:
            move_qty= rnd(1,28)
        print('Ход компьютера, компьютер выбирает: ',move_qty)
    if move_qty>28 or move_qty<1:
        print('Правила нарушены. Игра окончена')
        exit()
    
    total_qty-=move_qty
    print('Оставшееся кол-во =', total_qty)

if whos_move==1:
    print('Выиграл игрок')
else:
    print('Компьютер выиграл')