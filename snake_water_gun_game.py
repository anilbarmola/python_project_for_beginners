#***************snake water gun game programe********
import random
from secrets import choice
list=["snake","water","gun"]
choice=random.choice(list)
#yourchoice=int(input("1 for snake 2 for water and 3 for gun"))
yourchoice="water"
print("computer choice is:", choice)
print("your choice is :", yourchoice)

if choice=="snake" and yourchoice=="snake":
    print("Drow Game")
elif choice=="water" and yourchoice=="snake":
    print("!!!you Win!!!!")
elif choice=="gun" and yourchoice=="snake":
    print("!!!you win !!!!")
elif choice=="snake" and yourchoice=="water":
    print("!!!you win!!!")
elif choice=="water" and yourchoice=="water":
    print("Drow Game")
elif choice=="gun" and yourchoice=="water":
    print("!!!you win !!!!")
elif choice=="snake" and yourchoice=="gun":
    print("!!!you win!!!")
elif choice=="water" and yourchoice=="gun":
    print("!!!you Win!!!!")
elif choice=="gun" and yourchoice=="gun":
    print("Drow Game")
else:
    print("Please give correct input")