import random
import time
print('hi every one Welcome to the game ')
time.sleep(2)
n=random.randint(1,10)
print('Number has been generated  \n sir you have 4 chances to guess the number')


count=4
while count!=0:
    a=int(input('Guess the Number please:'))

    if a==n:
        print("yep!!! that is right . you won sir!") 
        break
    elif a > n:
        print('the number is less than',a)
    else:
        print('the number is greater than',a)
        count=-1  