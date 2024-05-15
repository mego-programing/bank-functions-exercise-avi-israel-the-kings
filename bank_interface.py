sum1 = 500
x1 = 0
y = 0


def deposit(x):
    global sum1
    sum1 += x
    return sum1


def attraction(x):
    global sum1
    if sum1 - x < 0:
        return False
    else:
        sum1 -= x
        return sum1


def status():
    global sum1
    print(sum1)


def My_Bank():
    global y
    global x1
    y = int(input("Hello !\n"
                  " If you want to withdraw money from your account tap 1.\n"
                  " If you want to deposit money in your account tap 2.\n"
                  " Check balance tap 3"))
    if y == 1:
        x1 = int(input("Please enter an amount"))
        print("This is the amount you currently have in your account",attraction(x1))
    elif y == 2:
        x2 = int(input("Please enter an amount"))
        print("This is the amount you currently have in your account", deposit(x2))
    elif y == 3:
        status()
    else:
        return False


My_Bank()
