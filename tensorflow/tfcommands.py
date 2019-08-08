y = tf.constant(39, name='y')                    # Define y. Set to 39
W = tf.constant(np.random.randn(4,3), name = "W")

init = tf.global_variables_initializer()         # When init is run later (session.run(init)),

Y = tf.add(tf.matmul(W,X), b)
sess = tf.Session()
result = sess.run(Y)
sess.close()

x = tf.placeholder(tf.int64, shape=(1024, 1024), name = 'x')
X = tf.placeholder(tf.float32, shape = (n_x, None), name = 'X') # matrice con n_x righe


tf.one_hot(labels, depth, axis)
# axis = 0 -> classi disposte in orizzontale, sulle righe
# axis = 1 -> classi disposte in verticale, sulle colonne

tf.get_variable(name, shape=None, dtype=None)

# It is important to know that the "logits" and "labels" inputs of tf.nn.softmax_cross_entropy_with_logits
# are expected to be of shape (number of examples, num_classes).

optimizer = tf.train.AdamOptimizer(learning_rate = learning_rate).minimize(cost)
