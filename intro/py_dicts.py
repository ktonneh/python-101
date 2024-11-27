# dictionaries

a = {
    "key":"value",
    "harry":"code",
    "marks":"100",
    "list":[2,3,4,5]
}

print('a ',a)
print('a[key]',a["key"])
print('a[list]', a["list"])

a.pop("key")



print("a ",a)
print('Items: ',str(a.items()))
print('Keys: ',str(a.keys()))
print('a[list]: ',a['list'])
print('a[list]: ',a.get('list'))

a.update({"harry":"codec"})
print('a[harry updated]',a.get('harry'))

print('Len>> ',a)
print('Len>> ',len(a))