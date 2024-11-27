# factorial of a number
# 5 = 5 * 4 * 3 *2 * 1
# 6 = 6 * 5 * 4 * 3 *2 * 1

num  = 6
fact = 1
for i in range(1,num+1):
    print('i >',i)
    fact *= i
    
print('Factorial of ',num,' = ',fact) 