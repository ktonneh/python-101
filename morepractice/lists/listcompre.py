nums = [10,20,30,40,50,60]
nums_double = []
for n in nums:
    nums_double.append(n*2)

# with list comprehension
nums_double = [n * 2 for n in nums]
print(nums_double)

print('-------------with conditions -----------')

nums_double =[n * 2 for n in nums if n % 4 ==0]


