# Intallation:
# $ pip3 install tensorflow

import os
import tensorflow as tf
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # 0 = all messages are logged (default behavior)
                                         # 1 = INFO messages are not printed
                                         # 2 = INFO and WARNING messages are not printed
                                         # 3 = INFO, WARNING, and ERROR messages are not printed

hello = tf.constant('Hello, Tensors!')
sess = tf.Session()
print(sess.run(hello)) # 'Hello, Tensors!'

# Mathematical computation
a = tf.constant(10)
b = tf.constant(32)
print(sess.run(a+b)) # 42

mat_1 = 10*np.random.random_sample((3, 4))   # Creating NumPy arrays
mat_2 = 10*np.random.random_sample((4, 6))

# Creating a pair of constant ops, and including the above made matrices
tf_mat_1 = tf.constant(mat_1)
tf_mat_2 = tf.constant(mat_2)

# Multiplying TensorFlow matrices with matrix multiplication operation
tf_mat_prod = tf.matmul(tf_mat_1 , tf_mat_2)
sess = tf.Session()            # Launching a session

# run() executes required ops and performs the request to store output in 'mult_matrix' variable
mult_matrix = sess.run(tf_mat_prod)
print(mult_matrix) # [[118.54634241  43.43291131  82.64194579  76.09971275 104.60032541   23.38257953]
                   #  [136.68239381  65.12882724 167.33261515 111.21662923 134.16910096   33.4861526 ]
                   #  [128.5460993   50.53790473 108.75633423  95.2062044  127.22209211   27.01027389]]

# Performing constant operations with the addition and subtraction of two constants
a = tf.constant(10)
a = tf.constant(20)
print("Addition of constants 10 and 20 is %i " % sess.run(a+b)) # Addition of constants 10 and 20 is 30
print("Subtraction of constants 10 and 20 is %i " % sess.run(a-b)) # Subtraction of constants 10 and 20 is -10

sess.close()                          # Closing the session

# Note: As no graph was specified in the preceding example with the
# TensorFlow, the session makes use of the default instance only.