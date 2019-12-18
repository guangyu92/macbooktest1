import tensorflow as tf
from mxnet import nd

a=tf.constant([1.])
b=tf.constant([4.])

x=nd.arange(4).reshape((4,1))

print(x)