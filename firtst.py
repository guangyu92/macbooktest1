import tensorflow as tf
from mxnet import nd

x=nd.arange(12)

m=x.reshape((3,4))

print(m)
print(x.size)


