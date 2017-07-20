
# coding: utf-8

# In[13]:

#basic neural network trained on performing XOR 

import numpy as np

#input data set as np array
X = np.array([[0,0,1], [0,1,1], [1,0,1], [1,1,1]])
#output data set of expected values
y = np.array([[0,0,1,1]]).T

#sigmoid function
def nonlinear(x,derivative=False):
    if(derivative==True):
        return x*(1-x)
    else:
        return 1/(1+np.exp(-x))

np.random.seed(1)

syn0 = 2*np.random.random((3,1)) - 1

for iter in xrange(10000):
    l0 = X
    l1 = nonlinear(np.dot(l0,syn0))
    
    l1_error = y - l1
    
    l1_delta = l1_error * nonlinear(l1, True)
    
    syn0 += np.dot(l0.T,l1_delta)
    
print "output after training"
print l1


# In[ ]:




# In[ ]:



