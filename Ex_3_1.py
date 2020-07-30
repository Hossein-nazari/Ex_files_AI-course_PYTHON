num=int(input('Inter a Year'))
if num%4!=0:
    print('kabise nist')
elif num%100==0 and num%400==0:
    print('kabise hast')
elif num%100==0 and num%400!=0:
     print('kabise nist')
else:
    print('kabise hast')