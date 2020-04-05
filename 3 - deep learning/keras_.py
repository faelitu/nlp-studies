# Keras is a highly modular neural networks library, which runs on top of
# Theano or TensorFlow. Keras is one of the libraries which supports both
# CNNs and RNNs (we will be discussing these two neural networks in detail
# in later chapters), and runs effortlessly on GPU and CPU.

# A model is understood as a sequence or a graph of standalone,
# fully configurable modules that can be plugged together with as little
# restrictions as possible. In particular, neural layers, cost functions,
# optimizers, initialization schemes, activation functions, regularization
# schemes are all standalone modules that could be combined to create new
# models.

# Installation:

# In addition to the Theano or TensorFlow as back end, Keras makes use
# of the few libraries as dependencies. Installing these before Theano or
# TensorFlow installation eases the process.

# $ pip3 install numpy scipy scikit-learn pillow h5py
# $ pip3 install keras

# Implementation Example:

# Importing the required libraries and layers and model from Keras
import keras
from keras.layers import Dense
from keras.models import Sequential
import numpy as np
# Dataset Link : # https://archive.ics.uci.edu/ml/datasets/Blood+Transfusion+Service+Center
# Save the dataset as a .csv file :
tran_ = np.genfromtxt('transfusion.csv', delimiter=',')
X=tran_[:,0:4]           # The dataset offers 4 input variables
Y=tran_[:,4]             # Target variable with '1' and '0'
print(X)

# Creating our first MLP model with Keras
mlp_keras = Sequential()

# As the input data has four corresponding variables, the input_dim,
# which refers to the number of different input variables, has been set to
# four.

# Here, the
# first hidden layer is made up of eight neurons, which are responsible for
# further capturing the nonlinearity.

# The second layer has six
# neurons and configurations similar to its previous layer.

mlp_keras.add(Dense(8, input_dim=4, init='uniform', activation='relu'))
mlp_keras.add(Dense(6, init='uniform', activation='relu'))

# In the last layer of output, we have set the activation as sigmoid,
# which is responsible for generating a value between
# 0 and 1 and helps in the binary classification.

mlp_keras.add(Dense(1, init='uniform', activation='sigmoid'))

# To compile the network, we have made use of the binary classification
# with logarithmic loss and selected Adam as the default choice of optimizer,
# and accuracy as the desired metric to be tracked. The network is trained
# using the backpropagation algorithm, along with the given optimization
# algorithm and loss function.

mlp_keras.compile(loss = 'binary_crossentropy', optimizer='adam',metrics=['accuracy'])

# The model has been trained on the given dataset with a small number
# of iterations (nb_epoch) and started with a feasible batch size of instances
# (batch_size). The parameters could be chosen either on the basis of prior
# experience of working with such kinds of datasets, or one can even make
# use of Grid Search to optimize the choice of such parameters.

mlp_keras.fit(X,Y, nb_epoch=200, batch_size=8, verbose=0)

# The next step is to finally evaluate the model that has been built and
# to check out the performance metrics, loss, and accuracy on the initial
# training dataset. The same operation could be performed on a new test
# dataset with which the model is not acquainted and could be a better
# measure of the model performance.

accuracy = mlp_keras.evaluate(X,Y)
print("Accuracy : %.2f%% " %  (accuracy[1]*100 ))

# Example 2:

# If one wants to further optimize the model by using different
# combinations of parameters and other tweaks, it could be done by using
# different parameters and steps while undertaking model creation and
# validation, though it need not result in better performance in all cases.

# Using a different set of optimizer
from keras.optimizers import SGD
opt = SGD(lr=0.01)

# The following creates a model with configurations similar to those in
# the earlier model but with a different optimizer and including a validation
# dataset from the initial training data:

mlp_optim = Sequential()
mlp_optim.add(Dense(8, input_dim=4, init='uniform', activation='relu'))
mlp_optim.add(Dense(6, init='uniform', activation='relu'))
mlp_optim.add(Dense(1, init='uniform', activation='sigmoid'))

# Compiling the model with SGD
mlp_optim.compile(loss = 'binary_crossentropy',
optimizer=opt, metrics=['accuracy'])

# Fitting the model and checking accuracy
mlp_optim.fit(X,Y, validation_split=0.3, nb_epoch=150, batch_size=10, verbose=0)
results_optim = mlp_optim.evaluate(X,Y)
print("Accuracy : %.2f%%" % (results_optim[1]*100 ) )