def merge_sorted_lists(list1, list2):
    merged_list = []
    i = j = 0

    
    # Merge the two lists
    while(i < len(list1) and j < len(list2)):
        if(list1[i] < list2[j]):
            merged_list.append(list1[i])
            i+=1
        else:
            merged_list.append(list2[j])
            j+=1
    # Append remaining elements (if any)
    merged_list.append(list1[i:])
    merged_list.append(list2[j:])
    
    return merged_list

# Test the function
list1 = [4, 6, 8, 10]
list2 = [3, 7, 11, 12]
print(merge_sorted_lists(list1, list2))  # Output: [3, 4, 6, 7, 8, 10, 11, 12]