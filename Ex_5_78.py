nums=[]
while len(nums)<3:
    nums.append(int(input('Enter a number : ')))
    print(nums)
if len(nums)==3:
    i=input('Do you still want save last number  ?  ')
    if i=='no':
        nums.pop(-1)
        print(nums)

print('Done!')