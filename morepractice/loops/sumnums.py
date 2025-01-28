def calculate_average(numbers):
    # Write your code here
    sum = 0
    for item in numbers:
      sum+=item
    
    return sum//len(numbers)

# Test your function with different lists
numbers_list = [10, 20, 30, 40, 50]
print(f"The average of {numbers_list} is {calculate_average(numbers_list)}")