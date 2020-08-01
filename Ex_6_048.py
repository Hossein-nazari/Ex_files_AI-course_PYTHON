compnum=50
l1=[]
i=int(input('Guess a number'))
while i!=50:
    if i<50:
        l1.append(i)
        print('You guess is too low')
        i=int(input('Guess a number'))
    elif i>50:
        l1.append(i)
        print ('Your guess is too high')
        i=int(input('Guess a number'))
print('well done,you took ',len(l1),' attempts')
