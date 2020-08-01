l1=['dorehami','khandevane','akhbar','mosabeghe mahalle']
for i in l1:
    print(i)
i1=input('Enter a Tv show :  ')
i2=int(input("Enter it's index for inserting in list  :  "))
l1.insert(i2, i1)
for i in l1:
    print (i)