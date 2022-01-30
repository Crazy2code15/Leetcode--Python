# Snake Water or Gun Game
import random
def win(computer, player):
    if computer==player:
        return None
    elif computer=='s':
        if player=='w':
            return False
        elif player=='g':
            return True
    elif computer=='w':
        if player=='g':
            return False
        elif player=='s':
            return True
    elif computer=='g':
        if player=='s':
            return False
        elif player=='w':
            return True

randnum = random.randint(1, 3)
print(randnum)
if randnum==1:
    computer ='s'
elif randnum ==2:
    computer ='w'
elif randnum==3:
    computer ='g'

player = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
a = win(computer,player)
print(f"computer chose {computer}")
print(f"player chose {player}")

if a==None:
    print("The game is a tie!")
elif a:
    print("You Win")
else:
    print("You Lose!")