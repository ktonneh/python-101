# Write a program using functions to find greatest of three numbers.
def largest(nums):
    largest = 0
    for item in nums:
        print(item)
        if item > largest:
            largest = item
    
    return largest

def main():
    nums = [2,3,10,5,4]
    print('Largest in ', nums, 'is: ',largest(nums),end="")
    print('')

main()
