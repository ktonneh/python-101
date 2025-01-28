# add item to the end

items = [1,2,3,4,5]

items.append(6)
print(items)
print('----------------------------')
num_list = [12,13,3,4,5,6]
num_list.insert(3,4)

print(num_list)
print('Delete pop()')
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
houses.pop()
print(houses)

print('remove()----------------')

houses.remove('Ravenclaw')

print(houses)

print('------Remove nested---------')
# For nested lists
populations = [["Winterfell", 10000], ["King's Landing", 50000],
               ["Iron Islands", 5000]]

populations.remove(["Winterfell", 10000])
print(populations)

