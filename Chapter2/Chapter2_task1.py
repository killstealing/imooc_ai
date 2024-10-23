a=1
b=2
print(a,b)

import matplotlib


from matplotlib import pyplot as plt
x=[1,2,3,4,5]
y=[10,20,30,40,60]
print(x,y)

# figurel=plt.figure()
# plt.plot(x,y)
# plt.show()

import numpy as np
a=np.eye(10)
print(a)
print(type(a),a.shape)
b=np.ones([10,10])
print(b)
c=a+b
print(c)
import pandas as pd

data=pd.read_csv('./data.csv')
print(data)
