import numpy as np
def calc(Target,Ouput):
    SSres  = np.sum((Target - Ouput)**2)
    SStot  = np.sum((Target - np.mean(Target))**2)
    R2     = (1 - SSres/SStot)
    return R2