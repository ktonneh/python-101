# recursion
# factorial

# 5 = 5 * 4 * 3 * 2 * 1


def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)

def fibb(n):
    if n==1:
        return 0
    if(n==2):
        return 1
    
    return fibb(n-1) + fibb(n-2)

num = 4
print(f"factorial of {num} is {factorial(num)}")
print('----------------')
print('')
print()

