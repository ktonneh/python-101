# 4. Write a program to find whether a given number is prime or not.

def isPrime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3== 0:
        return False
    
    i = 5
    while i * i <=num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

num = int(input('Enter a number btw 1 - 100\n'))

if(num  < 1):
    print(' Enter No btw 1 & 100')

if(num > 100):
    print('Enter no between 1 & 100\n')

print('is ',num, ' prime?', ':',isPrime(num))


