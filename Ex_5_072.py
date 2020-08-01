str1=input('Enter your first favorite food : ')
str2=input('Enter your second favorite food : ')
str3=input('Enter your third favorite food : ')
str4=input('Enter your forth favorite food : ')
dict1={1:str1,2:str2,3:str3,4:str4}
print (dict1)
a=int(input('Get ride one of foods which you selected  '))
if 1<a<5:
    dict1.pop(a)
    {k:v for k, v in sorted(dict1.items(),key=lambda item:item[1])}
    print(dict1)
    
else:
    print('wrong selection')