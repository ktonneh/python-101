'''
* * *
*   *     for n = 3
* * *
'''

n = 4

for i in range(n):
    #print('i>>',i)
    if i==0 or i == n-1:
        print('*' * n)
    else:
        print('*' + ' ' * (n-2) + '*')
