friends = ["apple",23,False,"john"]

print('Len: ',len(friends))
print(friends[:])
print(friends[0:])
print(friends[:5])
print(friends[1:5:2])
print(friends[0:2])

nums = [2,3,1,23,76,43,56,21,4,5]

nums.pop(1)
print('Nums: ',nums)

nums.insert(1,10)

print('Sum:', nums.sort())
#print('Sum:', nums.count())

for num in nums:
    print(num,'\n')

def capture_user_list():
    fruits = []
    size  = 7
    print('Capture the 7 fruits here')
    while size > 0:
        fruits.append(input('Enter Fruits'))
        size-=1
    
    print(fruits)

capture_user_list();

