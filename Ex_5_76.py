l1=[]
p1=input('Enter a name that you want invite him to a party  :  ')
l1.append(p1)
p2=input('Enter an other name that you want invite him to a party  :  ')
l1.append(p2)
p3=input('Enter the third name that you want invite him to a party  :  ')
l1.append(p3)
q1=input ('Do you wana add others to this list  ?  yes/no  ')
q1=q1.lower()
while q1=='yes':
    pn=input('Enter an other name,when is enough type no  ')
    if pn=="no":
        break
    l1.append(pn)
    print (l1)
print (l1)
q2=input('choose a person : ')
if q2  in l1:
    print(l1.index(q2))
    q3=input('do you still want this person come to the party ? ')
    if q3=='no':
        l1.remove(q2)
    else:
        print(l1)
else:
    print('wrong input')
    q2