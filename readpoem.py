# read poem

with open('poems.txt','r') as f:
    text = f.read()

print('Text Poem: ',text)
if "twinkle" in str(text):
    print(text,' contains twinkle')
else:
    print(str(text))
    print('Does not contain twinkle')