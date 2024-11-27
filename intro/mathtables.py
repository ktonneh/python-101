# math table and write to file
def open_file(filename,mode,content):
        with open('tables/'+filename,mode) as f:
                f.write(content+'\n')

for item in range(2,21):
    filename = "{}".format(item)+".txt" 
    # print(filename)
    for i in range(1,item+1):
           content = "{}  x ".format(i)+" {}".format(i)+" =  {}".format(i * i)
           #print(content)
           #print(i,' x ', i , '= ', i * i)
           open_file(filename,'a',content)

