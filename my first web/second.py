import tensorflow as tf
from mxnet import nd
import numpy as np

a=tf.constant([1.])
b=tf.constant([4.])

print(a+b)

x=nd.arange(4).reshape((4,1))

print(x)

data=[]
for i in range(100):
    x=np.random.uniform(-10.,10.)
    eps=np.random.normal(0.,0.1)
    y=1.477*x+0.089+eps
    data.append([x,y])
data=np.array(data)

def mse(b,w,points):
    totalError=0
    for i in range(0,len(points)):
        x=points[i,0]
        y=points[i,1]
        totalError+=(y-(w*x+b))**2
    return totalError/float(len(points))

def step_gradient(b_current,w_current,points,lr):
    b_gradient=0
    w_gradient=0
    M=float(len(points))
    for i in range(0,len(points)):
        x=points[i,0]
        y=points[i,1]
        b_gradient+=(2/M)*((w_current*x+b_current)-y)
        w_gradient+=(2/M)*x*((w_current*x+b)-y)
    new_b=b_current-(lr*b_gradient)
    new_w=w_current-(lr*w_gradient)
    return(new_b,new_w)