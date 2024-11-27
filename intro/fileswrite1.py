# write to an empty file

with open('names1.txt','a') as f:
    f.write('kim, jong, un, putin')

# names = f.read()
with open('names1.txt','r') as f:
    names = f.read()

print(names)