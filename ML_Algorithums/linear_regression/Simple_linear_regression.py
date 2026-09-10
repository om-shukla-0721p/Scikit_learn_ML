import numpy as np
import pandas as pd

class SLR_OLS:
    def __init__(self):
        self.m=None
        self.b=None

    def fit(self,X_train,y_train):
        mean_X=np.mean(X_train)
        mean_y=np.mean(y_train)

        num=0
        deno=0

        for i in range(X_train.shape[0]):
            num+=(X_train[i]-mean_X)*(y_train[i]-mean_y)
            den+=(X_train[i]-mean_X)**2
        self.m=num/deno
        self.b=mean_y-(self.m*mean_X)

        return (self.m,self.b)

    def predict(self,X_test):
        return (self.m*X_test)+self.b
    