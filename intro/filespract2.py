# read file and close automatically

with open('names.txt','r') as f:
    names = f.read()

print(names)
