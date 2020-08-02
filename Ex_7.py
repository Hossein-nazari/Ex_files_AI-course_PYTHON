"""
def fib(arg):
    if arg<0:
        print ('incorrect input')
    elif arg==1:
        return 0
    elif arg==2:
        return 1
    else:
        return fib(arg-1)+fib(arg-2)
        """
fib_list=[0,1]
for i in range(2,30):
    fib_list.append(fib_list[i-1]+fib_list[i-2])
    print(fib_list[i])