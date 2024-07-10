
def a(x, y):
    return x+y

def s(x, y):
    return x-y

def m(x, y):
    return x*y

def d(x, y):
    return x/y

print('Welcome to the calculator!')

calculating = False


while True:
    if not calculating:
        choice = input("enter choice(a,s,m,d): ")
        calculating = True
        num1 = int(input("Enter number: "))
    num2 = input("Enter number (c to clear): ")
    if num2=='c':
        calculating = False
        continue
    num2 = int(num2)
    exec(f"num1 = {choice}({num1},{num2})")
    print(num1)
