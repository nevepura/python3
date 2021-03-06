
# GRADED FUNCTION: normalizeRows
import numpy as np
from numpy import linalg as la

x = np.array([
    [0, 3, 4],
    [1, 6, 4]])

print(x.shape)

def normalizeRows(x):
    """
    Implement a function that normalizes each row of the matrix x (to have unit length).
    
    Argument:
    x -- A numpy matrix of shape (n, m)
    
    Returns:
    x -- The normalized (by row) numpy matrix. You are allowed to modify x.
    """
    
    ### START CODE HERE ### (≈ 2 lines of code)
    # Compute x_norm as the norm 2 of x. Use np.linalg.norm(..., ord = 2, axis = ..., keepdims = True)
    x_norm = la.norm(x, ord = 2, axis = 1, keepdims = True)
    # nota che la norma ha dimensione inferiore, con una sola colonna, quindi ha dim diversa rispettto a 
    print('x: '+ x)
    print('x_norm shape: '+ x_norm.shape)
    # Divide x by its norm.
    x = x / x_norm
    ### END CODE HERE ###
    return x


print("normalizeRows(x) = " + str(normalizeRows(x)))