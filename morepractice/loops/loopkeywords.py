# break, continue, pass

num_list = list(range(0, 10))
for num in num_list:
    if num == 3 or num == 6 or num == 8:
        continue
    print(num)


print('---------------------------')
num_list = list(range(20))

for num in num_list:
    pass # You can write code here later on

print(len(num_list)) 