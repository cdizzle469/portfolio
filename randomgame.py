import random

num1 = int(input('enter start number: '))
num2 = int(input('enter end number: '))

secret_number = random.randint(num1,num2)

guess = int(input('enter number: '))

while True:
    guess = int(input('enter number: '))
    if guess<secret_number:
        print('higher')
    elif guess>secret_number:
        print('lower')
    else


print('You guessed correctly')