import numpy as np
import tensorflow as tf

array_dim = 1000
point_array = []

for i in range(array_dim):
    x1 = np.random.normal(0.0, 0.5)
    y1 = x1 * 0.1 + 0.3 * np.random.normal(0.0, 0.3)
    point_array.append([x1, y1])

array_x = [v[0] for v in point_array]
array_y = [v[1] for v in point_array]

print(point_array)

W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y = W * array_x + b

loss = tf.reduce_mean(tf.square(y - array_y))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

for step in range(100):
    sess.run(train)
    print(step, sess.run(loss), sess.run(W), sess.run(b))

