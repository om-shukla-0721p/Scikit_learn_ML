import numpy as np
X=np.array([1,2,3,4,5])
y=np.array([5,7,9,11,13])

def linear_regression(X,y,new_x):
    # initializing parameters
    theta_0=0 # intercept
    theta_1=0 # slope

    # Hyperparameters
    learning_rate=0.01 # alpha
    epochs=1000 # no. of iterations how close to minimum of cost functions
    m=len(X)

    for i in range(epochs):
        # prediction
        y_pred=theta_0+(theta_1)*X

        #error
        error=y_pred-y

        # Gradients
        d_theta_0=(1/m)*np.sum(error)
        d_theta_1=(1/m)*np.sum(error*X)

        # update
        theta_0=theta_0-learning_rate*(d_theta_0)
        theta_1=theta_1-learning_rate*(d_theta_1)

    # Test Prediction
    new_y=theta_0+theta_1*(new_x)
    return new_y

# print(linear_regression(X,y,6))


# again from memory

def Linear_regression(X,y,new_x,learning_rate=0.01,epochs=1000):
    # initializing theta
    theta_0=0 # intercept
    theta_1=0 # slope
    

    # Hyper(parameters)
    # learning_rate=0.01
    # epochs=1000
    m=len(X)

    for i in range(epochs):
        # prediction 
        y_pred=theta_0+theta_1*X

        # error
        error=y_pred-y

        # gradient
        d_theta_0=(1/m)*(np.sum(error))
        d_theta_1=(1/m)*(np.sum(error*X))

        # new theta_0 and theta_1 updation
        theta_0=theta_0-(learning_rate)*d_theta_0
        theta_1=theta_1-(learning_rate)*d_theta_1
        # print(theta_0,theta_1) # to see the working very important and cool

    # Test Prediction
    new_y=theta_0 + new_x*(theta_1)
    return theta_0,theta_1

print(Linear_regression(X,y,6))



# performance

def r2_score(y,y_pred):
    SS_total=np.sum((y-np.mean(y))**2)

    ss_residual=np.sum((y-y_pred)**2)

    r2=1-(ss_residual/SS_total)
    return r2


def adjusted_r2(r2,n,p):
    r2=1-(((1-r2)*(n-1))/(n-p-1))
    return r2




X_test=np.array([12,3,4,62,2,4,2,4,53,2,4])
c,m=Linear_regression(X,y,6)
y_test=X_test*m +c

y_pred=X_test*m  + c 


r2=r2_score(y_test,y_pred)
ad_r2=adjusted_r2(r2,5,1)

print("R2:",r2)
print("R2_Adjusted:",ad_r2)

        





