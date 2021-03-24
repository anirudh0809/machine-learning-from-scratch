import numpy as np
import matplotlib.pyplot as plt

def pred(m,X,b):
    return m*X + b

def error(b,m,X,Y):
    return m*X -b

def sum_sq_mean_error(m,b,X,Y):
    errored_term = 0
    number_of_elements = len(X)
    for i in range(number_of_elements):
        errored_term += error(b,m,X[i],Y[i])
    return errored_term

def fit(X,Y):
    mean_of_X = np.mean(X)
    mean_of_Y = np.mean(Y)
    total_number_of_values = len(X)
    corr = 0
    stdev =0
    for i in range(total_number_of_values):
        corr += ((X[i]-mean_of_X)*(Y[i]-mean_of_X))
        stdev += (X[i]-mean_of_X)**2
    m = corr/stdev
    b= mean_of_Y - (m*mean_of_X)
    return m,b

    




if __name__ == '__main__':
    X = [0.0,0.2,0.4,0.6,0.8,0.11,0.12,0.14,0.16]
    Y = [22,54,66,12,44,86,99,52,11]
        
    m,b = fit(X,Y)

    print("Value of m =",m)
    print("\n")
    print("Value of b =",b)
    print("----------------------------------------------")

    error =sum_sq_mean_error(m,b,X,Y)

    print("Sum of squared mean error =",error)

    # Predictions on a value of X
    prediction=pred(m,85,X)
    print("Predicted value =",prediction)

    max_x = np.max(X)
    min_x = np.min(X)

    x= np.linespace(min_x,max_x,10000)
    y = b + m* x
    plt.plot(x, y, color='#00ff00', label='Linear Regression')
    #plot the data point
    plt.scatter(X, Y, color='#ff0000', label='Data Point')
    # x-axis label
    plt.xlabel('X')
    #y-axis label
    plt.ylabel('Y')
    plt.legend()
    plt.show()







        
