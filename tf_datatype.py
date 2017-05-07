import tensorflow as tf

a = tf.random_uniform([10, 2], -1.0, 1.0)
b = tf.expand_dims(a, 0)
c = tf.expand_dims(a, 1)
d = tf.expand_dims(a, 2)

sess = tf.Session()
print('tf.shape(a)', sess.run(tf.shape(a)))
print('tf.shape(b)', sess.run(tf.shape(b)))
print('tf.shape(c)', sess.run(tf.shape(c)))
print('tf.shape(d)', sess.run(tf.shape(d)))

print('a', sess.run(a))
print('b', sess.run(b))

