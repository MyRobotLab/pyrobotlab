f = open('Index.csv','r')
a = ['0','1']
lst = []
for line in f:
    for word in a:
        if word in line:
            line = line.replace(word,'')
    lst.append(line)
f.close()
f = open('Index.csv','w')
for line in lst:
    f.write(line)
f.close() 
