counter = 1
while counter <= 5:
    print(counter)
    counter+=1

print('-----------------------')

n = 9015

while n > 0:
    digit = n % 10
    print(digit,end=' ')
    n = n // 10