import random
print("this game to guess a number from the dice and then the dice is thrwon. if you guess the same number as outcomeon the dice u won. if not u lose")
b=1
while b==1:
    a=int(input("entre any number between 1 to 6:n"))
    x=random.randint(1,6)
    if 1<=a<=6:
        if a==x:
            print(" CONGRATS! you won. ")
        else:
                print("BETTER LUCK NEXT TIME! computer generated number is ",x)
    else:print("entre a number between 1 and 6")
b=int(input("want to play more entre 1 and for exit entre 0:"))