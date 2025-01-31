# Creating a set with duplicate elements

# unique elements
elements = {1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 9}
print(elements)

# Union
#  Define two sets
set_A = {1, 2, 3, 4}
set_B = {'a', 'b', 'c', 'd'}

print('----Union----')
print(set_A | set_B)
print(set_A.union(set_B))
print('----End Union---')

print('----Intersection----')
print(set_A | set_B)
print(set_A.intersection(set_B))
print('----End Intersection---')