# A file contains a word “Donkey” multiple times.  You need to write a program which replace Donkey with ##### by updating the same file.

with open('donkeyfile.txt','r') as f:
    text = f.read()

print('text: ',text)


text = text.replace('Donkey','#####')
with open('donkeyfile.txt','w') as f:
    f.write(text)

with open('donkeyfile.txt','r') as f:
    text = f.read()


print('final text: ',text)

