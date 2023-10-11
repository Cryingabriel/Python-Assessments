import winsound



def countbythree():
    y = 6
    for i in range(11):
        print(y)
        y += 3

countbythree()
countbythree()

def exercisecheck():
    l = int(input("How many minutes of exercise do you get every week? "))

    if l <= 20:
        print("That's not enough exercise.")
    elif l > 20 and l <= 100:
        print("You should get a bit more exercise.")
    elif l > 100 and l <= 500:
        print("You got the perfect amount of exercise.")
    else:
        print("That's a lot of exercise, you should make sure to drink plenty of water.")

exercisecheck()


def Userbeeps(num):
    for i in range(num):
        winsound.Beep(480,200)

l = int(input("How many beeps do you want to hear? "))

Userbeeps(l)