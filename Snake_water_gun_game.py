

from random import randint

#0-snake, 1-water,2-gun

rand =randint(0,2)
if rand==0:
    comp='s'
if rand==1:
    comp='w'
if rand==2:
    comp='g'

def gamewin(comp,you):
    if you==comp:
        return None
    elif you=='s':
        if comp=='w':
            return True
        elif comp=='g':
            return False
    elif you=='w':
        if comp=='s':
            return False
        elif comp=='g':
            return True
    elif you=='g':
        if comp=='s':
            return True
        elif comp=='w':
            return False
while True:
    you=input('Choose snake (s), water (w), Gun (g), exit_game(e)\n')
    if you == 'e':
        break
    else:
        print(f'You chose {you}')
        print(f'Computer chose {comp}')
        if gamewin(comp,you) ==None:
            print('Game is tie')
        elif gamewin(comp,you)==True:
            print('You won!!')
        elif gamewin(comp,you)==False:
            print('You lost :(')



    

    


