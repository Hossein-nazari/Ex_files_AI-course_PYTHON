def fib(i):
    if(i==0):
        return 0
    elif(i==1):
        return 1
    else:
        return (fib(i-2)+fib(i-1))
    
def fib_list(i):
    l1=[]
    for i in range(0, i+1):
        l1.append(fib(i))
    return (l1)

i=int(input('Enter a number : '))  
print(fib(i))
print(fib_list(i))