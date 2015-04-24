import numpy as np
class Normalization:
    def __init__(self, X):
        self.mu     = np.mean(X,axis = 0)
        self.sigma  = np.std(X,axis = 0)
    
    def norm(self,X):    
        mu      = np.ones(X.shape, dtype = 'float')
        sigma   = np.eye(X.shape[1], dtype = 'float')
        for i in range(X.shape[1]):
            mu[:,i] = self.mu[i]*mu[:,i]
            sigma[i,i] = 1/self.sigma[i]   
        return np.dot((X - mu),sigma)