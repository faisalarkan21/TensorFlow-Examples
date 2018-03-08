import tensorflow as tf

const = tf.constant(2.0)

# b and c should using tf.global_variables_initializer()
b = tf.Variable(2.0)
c = tf.Variable(1.0)

d = tf.add(b, c)
e = tf.add(c, const)
a = tf.multiply(d, e)

# for init Variable not constant
init_op = tf.global_variables_initializer()

# start the session
with tf.Session() as sess:
    # initialise the variables
    sess.run(init_op)
    # compute the output of the graph
    a_out = sess.run(a)
    print("Variable a is {}".format(a_out))



