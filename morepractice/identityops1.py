original_list = [1,2,3]

same_ref_list = original_list

different_list = [1,2,3]

reorderedlist = [1,3,2]


print('original_list is_same_reference_list: ',original_list is same_ref_list)
print('original_list is different_list: ',original_list is different_list)

print('original_list == different_list: ',original_list == different_list)
print('original_list == reordered_list: ',original_list == reorderedlist)


first_number = 10
second_number = 20
third_number = 10

print('first_number is not second_number: ',first_number is not second_number)
print('first_number is not 10: ',first_number is not 10)
print('first_number is not third_number: ',first_number is not third_number)
print('first_number is third_number: ',first_number is  third_number) # Integer interning -> memory efficiency small integer literals(pool)
