odd_list = [1, 3, 5, 7]
unordered_set = {9, 10, 11, 12, 13, 14, 15, 16, 17}

for item in unordered_set:
    if item % 2 != 0:
        odd_list.append(item)


print(odd_list)