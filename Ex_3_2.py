# detecting day of year and leaf years
day=int(input('Enter a day : '))
month=int(input('Enter a Month : '))
year=int(input('Enter a year : '))
l1=[31,29,31,30,31,30,31,31,30,31,30,31]
if year%400==0 or (year%4==0 and year%100!=0):
    l1[1]=29
    print(sum(l1[:month-1])+day)
    print('leaf year')   
else:
    l1[1]=28
    print(sum(l1[:month-1])+day)
    print('normal year')