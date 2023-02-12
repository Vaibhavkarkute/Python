import random

def gameWin(comp,you):

    #if the two value are same , declare as tie !
    if comp==you:
        return None
    # Check for all possibilities when computer chose st
    elif comp =='stone':
        if you=='paper':
            return True
        elif you =='sizer':
            return False
    # Check for all possibilities when computer chose p
    elif comp=='paper':
        if you=='sizer':
            return True
        elif you =='stone':
            return False
    # Check for all possibilities when computer chose si
    elif comp=='sizer':
        if you =='paper':
            return True
        elif you =='stone':
            return False



print ("Comp Turn : Stone (st) Paper (p) And Sizer (si) :")
randNo = random.randint(1,3)
if randNo==1:
    comp = 'stone'
elif randNo==2:
    comp = 'paper'   
elif randNo==3:
    comp = 'sizersto'    

you = input("You Turn : Stone(st) Paper(p) And Sizer(si) :")
a=gameWin(comp,you)

print (f"Comp chose {comp}")
print (f"You chose {you}")

if a== None:
    print(" The game is Tie ! ")
elif a:
    print("You Win")
else:
    print("You Lose")
