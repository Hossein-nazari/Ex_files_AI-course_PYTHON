l=[]
i1=input('who you want invite to the party ? ')
l.append(i1)
print(i1,'|',len(l),'person invited')
q1=input('Do you wana add somebody to list? (y/n)')
while q1=='y':
    i2=(input('Enter a name : '))
    l.append(i2)
    for i in l:
        print (i)
    print(len(l),'person invited')
    q1=input('Do you wana add somebody to list? (y/n)')
print(len(l),'person invited')