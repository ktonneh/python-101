def count_low_high(num_list):
  # Write your code here
    low = 0
    high = 0
    list_count = []
    for item in num_list:
        if item > 50 or item % 3 == 0:
            high+=1
        else:
            low+=1

    list_count.append(low)
    list_count.append(high)
    return list_count
    

num_list = [20, 9, 51, 81, 50, 42, 77]
print(count_low_high(num_list))