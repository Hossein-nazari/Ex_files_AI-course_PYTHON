l1=[]
i=int(input('Enter a number : '))
i2=int(input('Enter an other number : '))
l1.append(i)
l1.append(i2)
i3=input ( 'if you want ass other number enter "y" ')
i3.lower()
if i3=='y':
    while i3=='y':
        i4=int( input('Enter a number : '))
        l1.append(i4)
        i3=input ( 'if you want ass other number enter "y" ')
        i3.lower()
    print("total is " , sum(l1))
else:
    print(sum(l1))
