l1=[234,876,345,684]
for i in l1:
      print (i)
a=int(input('enter a three-digital number  :  '))
if a in l1:
    print(l1.index(a))
else:
    print('that is not in the list')