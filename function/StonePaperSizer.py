import random

def gameWin(comp,you):

    #if the two value are same , declare as tie !
    if comp==you:
        return None
    # Check for all possibilities when computer chose r
    elif comp =='rock':
        if you=='paper':
            return True
        elif you =='scissors':
            return False
    # Check for all possibilities when computer chose p
    elif comp=='paper':
        if you=='scissors':
            return True
        elif you =='rock':
            return False
    # Check for all possibilities when computer chose si
    elif comp=='scissors':
        if you =='paper':
            return True
        elif you =='rock':
            return False



print ("Comp Turn : rock (r) Paper (p) And scissors (si) :")
randNo = random.randint(1,3)
if randNo==1:
    comp = 'rock'
elif randNo==2:
    comp = 'paper'   
elif randNo==3:
    comp = 'scissors'    

you = input("You Turn : rock(r) Paper(p) And scissors(si) :")
a=gameWin(comp,you)

print (f"Comp chose {comp}")
print (f"You chose {you}")

if a== None:
    print(" The game is Tie ! ")
elif a:
    print("You Win")
else:
    print("You Lose")
