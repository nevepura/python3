'''
Binary Contiguous Array

works but slow
'''
# get the length of the max binary contiguous array
def binarray(arr):
    
    if len(arr) == 0:
        return 0
    
    if (bca(arr)):
        return len(arr)
    
    return max(binarray(arr[:-1]), binarray(arr[1:]))
        
        
# check if an array is a binary contiguous array        
def bca(arr):
    ones = arr.count(1)
    zeros = arr.count(0)
    return ones == zeros
