
phone_book = dict(alusa=2345353)

phone_book = {
    'john':323252523,
    'doe':435353424,
    'Charlie': 456464
}

print(phone_book)

print(phone_book.get('john'))

phone_book['john'] = 11111111

print(phone_book)

del (phone_book['doe'])

print(phone_book)

print(len(phone_book))

charlie = phone_book.pop('Charlie')
charlie = phone_book.popitem()

print(charlie)

second_phone_book = {"Catwoman": 67423, "Jaime": 237734, "Godzilla": 37623}

phone_book.update(second_phone_book)


print(phone_book)

print(phone_book.items())