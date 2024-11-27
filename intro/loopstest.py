# Write a program to print multiplication table of a given number using for loop.

num = int(input('Enter a number btw 1 - 10'))

if(num  < 1):
    print(' Enter No btw 1 & 10')

if(num > 10):
    print('Enter no between 1 & 10')

i = 1
while(i <= 10):
    print(i,'x',num,i * num)
    i +=1


    