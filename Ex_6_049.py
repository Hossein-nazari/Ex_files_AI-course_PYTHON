i=int(input('Enter a number between 10 to 20 : '))
while not 10<i<20:
    if i<10:
        print('too low')
        i=int(input('Enter a number between 10 to 20 : '))
    elif i>20:
        print('too high')
        i=int(input('Enter a number between 10 to 20 : '))
print('thank you')
