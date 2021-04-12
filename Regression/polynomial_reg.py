
import numpy as np 
import sys 
import scipy 
from collections import OrderedDict

class poly:
    def __init__(self,X,Y):
        self.x = X 
        self.y = Y

    def cost_computaion(self):
        pass

    def hypothesis_testing(self,theta,X):
        hypo = theta[0]

        for i in np.arrage(1,len(theta)):
            hypo += theta[i]
        pass
