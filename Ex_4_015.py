str1=input('Hi dear, Is it rainy today? ')
str1=str1.lower()
if (str1=="yes"):
    str2=input('Is it windy too? ')
    str2=str2.lower()
    if str2=="yes" :
        print("It's too windy for an umbrella . ")
    else:
        print("Take an umbrella")
else:
    print("Enjoy you'r day:)")