import numpy as np 
import os
import time 


class gradient_regression():

    def __init__(self):
        self.learning_rate = 1e-2
        self.max_iterations = 10000
        

    def prediction(self,X,weight):
        return np.dot(weight.T,X)

    def losses(self,prediction,y):
        loss = 1/self.m * np.power(prediction - y,2)
        return loss

    def gradient_descent(self,weight,X,y,prediction):
        D_loss_Dw = 2/self.m * np.dot(X,(prediction -y).T)

        weight = weight - self.learning_rate * D_loss_Dw
        return weight

    def main(self,X,y):
        x1 = np.ones((1, X.shape[1]))
        X = np.append(X,x1,axis=0)

        self.m = X.shape[1]
        self.n = X.shape[0]

        weight = np.zeros((self.n,1))

        for iteration in range(self.max_iterations+1):
            pred = self.prediction(X,weight)
            loss = self.losses(pred,y)

            if iteration % 2000 == 0:
                print(f'Loss at iteration {iteration} is {loss}')

            weight = self.gradient_descent(weight,X,y,pred)

        return weight

    
if __name__ == '__main__':
    X = np.random.rand(1,500)
    y = 4 * X + np.random.rand(1,500) * 0.1

    LR = gradient_regression()
    weight = LR.main(X,y)
