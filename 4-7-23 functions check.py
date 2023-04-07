import random


def monsetrgen():
    y = random.randint(0,100)
    if y < 20:
        print("You encounter a Skeleton!")
    elif y < 50:
        print("You encounter a Zombie")
    elif y < 60:
        print("You encounter a Witch")
    else:
        print("You are safe!... for now.")

quit = False

while quit == False:  
    e = input("Type quit to end loop")
    if e == "quit":
        quit = True
    else:
        monsetrgen()