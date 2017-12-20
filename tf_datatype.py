import tensorflow as tf

a = tf.random_uniform([4, 2], -2.0, 2.0)
b = tf.expand_dims(a, 0)
c = tf.expand_dims(a, 1)
#d = tf.expand_dims(a, 2)

sess = tf.Session()
sess.run()

print('a', a)
print('b', b)
print('c', c)

#print('tf.shape(a)', sess.run(tf.shape(a)))
#print('tf value of a', sess.run(a, b, c))
#print('tf value of b', sess.run(b))
#print('tf value of c', sess.run(c))

#print('tf.shape(b)', sess.run(tf.shape(b)))
#print('tf.shape(c)', sess.run(tf.shape(c)))
#print('tf.shape(d)', sess.run(tf.shape(d)))

#print('b', sess.run(b))


