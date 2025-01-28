# print 1 t0 10

for i in range(4):
    print(i)
print('--------------------------')    

# print 1 t0 10
print('--------------------------')
for i in range(0,10):
    print(i+1)


print('--------------------------')
for i in range(1,11,2):
    print(i)

print('--------------------------')

for i in range(1,11):
    if(i%2==0):
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

print('--------------------------')

float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
for item in range(0,len(float_list)):
    print(float_list[item],end=',')

print('--------------------------')
string_list = ["Hello", "World", "Educative", "Learning", "Platform"]
for str in string_list:
    print(str)

print('--------------------------')