'''
Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*

'''

n = 3

for item in range(n):
    print('*' * n)
    n-=1
