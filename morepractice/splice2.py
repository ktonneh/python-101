url1 = "https://www.example.com"
url2 = "ftp://ftp.example.org"
url3 = "http://api.example.net"

protocol1 = url1[:url1.index(':')]

print('Url 1 Protocol: ', protocol1)


protocol2 = url2[:url2.index(':')]

print('Protocol2: ',protocol2)


filename = "data_2022_01_15.csv"

extension = filename[filename.index('.')+1:]

print('Extension: ',extension)