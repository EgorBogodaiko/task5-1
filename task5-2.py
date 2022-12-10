
from random import randint as rnd

def print_current_field(field):
    print('-------------')
    print('|',field[1],'|',field[2],'|',field[3],'|')
    print('-------------')
    print('|',field[4],'|',field[5],'|',field[6],'|')
    print('-------------')
    print('|',field[7],'|',field[8],'|',field[9],'|')
    print('-------------')

def put_symbol(field,choise,who):
    if who == 1:
        sym='X'
    else:
        sym='O'
    while field[choise] =='X' or field[choise]=='O' or choise>9 or choise<1:
        print('Ячейка занята, либо не существует, выбери другую.')
        choise=int(input(f'Игрок {whos_move} выбирает ячейку: '))
    field[choise]=sym
    return field

def check_if_win(field,who):
    win=0
    if who == 1:
        sym='X'
    else:
        sym='O'
    if field[1]==sym and field[2]==sym and field[3]==sym:
        return who
    if field[4]==sym and field[5]==sym and field[6]==sym:
        return who
    if field[7]==sym and field[8]==sym and field[9]==sym:
        return who
    if field[1]==sym and field[4]==sym and field[5]==sym:
        return who
    if field[2]==sym and field[5]==sym and field[8]==sym:
        return who
    if field[3]==sym and field[6]==sym and field[9]==sym:
        return who
    if field[1]==sym and field[5]==sym and field[9]==sym:
        return who
    if field[7]==sym and field[5]==sym and field[3]==sym:
        return who
    return win
    
current_field=[]
i=0
while i<10:
    current_field.append(i)
    i+=1
print('Пустое поле с индексами для указания выбора: ')
print_current_field(current_field)

jereb=rnd(1,20)
if jereb%2>0:
    print("Жеребьёвкой выбран Игрок 1, он же X")
    whos_move=1
else:
    print("Жеребьёвкой выбран Игрок 2, он же О")
    whos_move=2

winner=0
i=0

while winner==0 and i<9:
    cell_choice=int(input(f'Игрок {whos_move} выбирает ячейку: '))
    field=put_symbol(current_field,cell_choice,whos_move)
    print_current_field(field)
    winner=check_if_win(current_field,whos_move)
    if whos_move==1:
        whos_move=2
    else:
        whos_move=1
    i+=1

if winner>0:
    print('Выиграл игрок ',winner)
elif i==9:
    print ('Ничья.')

