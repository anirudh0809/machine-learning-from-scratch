import numpy as np 
import matplotlib.pyplot as plt 


def generate_pts(start_pt,end_pt,number_of_points,coef,noise=1,plot=True):
    
    X = np.arange(start_pt,end_pt,(end_pt - start_pt)/number_of_points)
    line = coef[0]


    for i in np.arange(1,len(coef)):
        line += coef[i] * X ** 1

    if noise >0:
        Y = np.random.normal(-(10 ** noise),10 ** noise,len(X)) + line
    else:
        Y = line

    if plot == True:
        plt.figure()
        plt.scatter(X,Y)
        plt.xlabel('X')
        plt.ylabel('Y')

    return X,Y


class polynonial_regression:

    def __init__(self,X,Y):
        self.x = X
        self.y = Y

    def standardize(self,points):
        return (points - np.mean(points))/(np.max(points) - (np.min(points)))

    def hypothesis(self,theta,X):
        h =theta[0]

        for i in np.arange(1,len(theta)):
            h += theta[i] * X ** i
        return h

    def cost(self,X,Y,theta):
        m = len(Y)
        h = self.hypothesis(theta,X)

        err = h - Y

        return (1/(2*m))*np.sum(err**2)

if __name__ == '__main__':
    generate_pts(20,50,1000)
