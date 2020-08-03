def dayfinder (d,m,y):
    i = [31,28,31,30,31,30,31,31,30,31,30,31]
    if y%400==0 or (y%4==0 and y%100!=0):
        i[2]+=1
    return sum(i[:m-1])+d
    
print(dayfinder(3, 8, 2002))