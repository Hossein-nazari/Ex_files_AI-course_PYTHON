l1=['blue','red','green','yellow','black','white','gray','orange','purple','aqua']
print (l1)
a=int(input('Enter a number between 0 to 4 :  '))
if not 0<a<5:
    print('wring number')
b=int(input('Enter a number between 5 to 9 : '))
if not 5<b<10:
    print('wring number')
print (l1[a:b+1])