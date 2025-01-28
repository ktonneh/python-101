n = 50
num_list = [10, 25, 4, 23, 6, 18, 27, 47]
found = False
for n1 in num_list:
    for n2 in num_list:
        if(n1 != n2):
            if(n1 + n2 == n):
                found = True
                break
    if(found):
        print(f"Martching Pair Found: {n1},{n2}")
        break
    else:
        print('No Pair Found')

print('------------------------')
print(num_list)


str = '((())))'
start = 0
end = len(str) - 1
isBalanced = True

while(start < end):
    print(f"start: {start} - end: {end}")
    print(f"start: {str[start]} - end: {str[end]}")
    if num_list[start] != num_list[end]:
            start+=1
            end-=1
            continue
    else:
         isBalanced = False

print(f"isBalanced: {isBalanced}")


    