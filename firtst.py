import tensorflow as tf
from mxnet import nd

x=nd.arange(12)

m=nd.arange(12)

s=x*m
print(s)
print(m)
print(x.size)


