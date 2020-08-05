class time:
    def __init__ (self,hour_value=0,minute_value=0,secound_value=0):
        self.hour=hour_value
        self.minute=minute_value
        self.secound=secound_value
    def __str__ (self):
         return str(self.hour)+':'+str(self.minute)+':'+str(self.secound)
    def show(self):
        return self.hour,self.minute,self.secound
    def __repr__(self):
        return str(self.hour)+':'+str(self.minute)+':'+str(self.secound)
    def __add__(self,other):
        a=self.secound+other.secound
        b=self.minute+other.minute
        c=self.hour+other.hour
        if a>=60:
            b+=a//60
            a=a%60
        else:
            a=a
        if b>=60:
            c+=b//60
            b=b%60
        else:
            b=b
            return str (c)+':'+ str (b)+ ':' + str (a)
    def __sub__(self,other):
        a=self.secound-other.secound
        b=self.minute-other.minute
        c=self.hour-other.hour
        if a<0:
            b-=1
            a+=60
        if b<0:
            b+=60
            if c<=0:
                c+=1
            else:
                c-=1
        return str (c)+':'+ str (b)+ ':' + str (a)
t1=time(2,32,48)
t2=time(4,4,50)
print(t1+t2)
'''
t1.h=int(input('Enter hour : '))
t1.m=int(input('Enter min : '))
t1.s=int(input('Enter sec : '))
   
print(time.show(t1))
'''