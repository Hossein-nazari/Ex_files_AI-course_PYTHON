import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10)
print (x)
y1=(np.e**(-x/10))*(np.sin(x))
y2=x*np.e**(-x/3)

plt.figure()
plt.subplot(2,1,1)
plt.plot(x,y1,label='f(x)')
plt.legend()
plt.subplot(2,1,2)
plt.title('practice 10')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.plot(x,y2,label='g(x)')
plt.legend()
plt.title('practice 10')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()