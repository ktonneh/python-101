num_list = [0,2,3,4,5,6]

squared_nums = map(lambda num: num * num if num%2==0 else num,num_list)

squared_nums = list(squared_nums)

print(squared_nums)

