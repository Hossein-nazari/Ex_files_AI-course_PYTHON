year = int(input("yek adad vared konid"))
if not(year%4==0):
    print ("kabise nist")
elif not (year%100==0):
    print ("kabise hast")
elif not (year%400==0):
    print ("kabise nist")
else :
    print ("kabise hast")
