import datetime
letter = '''Dear <|Name|>,\n
You are selected! \n
<|Date|>
'''

letter = letter.replace('<|Name|>','John Doe')

letter = letter.replace('<|Date|>',str(datetime.datetime.now().strftime('%c')))

print(letter)