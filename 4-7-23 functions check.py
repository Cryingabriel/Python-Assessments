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
    e = input("Type quit to end loop ")
    if e == "quit":
        quit = True
    else:
        monsetrgen()

def ATDS(x,y):
    r = ((x+y)+2)/6
    return r

print(ATDS(5.0,2.5))


food = ["speget","brug", "chick tend", "fried rings", "Ice cream", "Sesame chicken", "doughnuts", "Chinese Food"]

print([food[2]])
food.append("Tacos")
print(len(food))
print(food)

pet = []

quit2 = False

while quit2 == False:
    l = input("What is the name of your pet, once done tpye quit ")
    if l == "quit":
        quit2 = True
    else:
        pet.append(l)

pet.sort()
print(pet)


for i in range(-20, 45, 5):
    print(i)

for i in range(5):
    for j in range(2):
        print("*", end='')
    print()

n = 50
while n != -10:
    print(n)
    n-=10

s = False
while s == False:
    l = input("do you want a Cookie")
    if l == "Yes":
        print("Here's a cookie")
    else:
        s = True