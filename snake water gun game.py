import random
def gamewin(comp,your):
    if comp==your:
        return None
    elif comp=='s':
        if your=='w':
            return False
        elif your=='g':
            return True
    elif comp=='w':
        if your=='s':
            return True
        elif your=='g':
            return False
    elif comp=='g':
        if your=='s':
            return False
        elif your=='w':
            return True

randomno=random.randint(1,3)
#print(randomno)
if randomno==1:
    comp='s'
elif randomno==2:
    comp='w'
elif randomno==3:
    comp='g'

your= input("your turn: snake(s) water(w) gun(g)")

a=gamewin(comp,your)

if a==None:
    print("Game is tie")
elif a:
    print("You win")
else:
    print("you lose")
