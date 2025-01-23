from functools import reduce
nums = [1,2,3,4,5,6]

result = reduce(lambda x,y: x + y,nums)

print(f"the sum of nums is {result}")