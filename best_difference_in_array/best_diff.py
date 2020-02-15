"""
Given an array, find the indexes (i,j) of the elements of the array that comply to:
    i < j
    A[j] - A[i] is max
    
In other words, find the two elements of the array of which the difference is maximum, given that i < j.


SOLUTION
Lets split it into distinct cases.
    CASES
    1) A has < 2 elements:
        Unlucky! No distinct elements -> no solution.
        
    2) A has exactly 2 elements:
        Then the solution must be these only elements
            i = 0
            j = 1
            
    3) A has more than 2 elements (the funny part):
        Let's say that A has n elements.
        In this case the solution is the best between 2:
        - best_diff(A[n-1])
        - {i = index of the minimum element in A[n-1], j = n}
        
        Starting from the array of 3 elements, we compare
        the first solution (in A[0..1])
        with the second, made by A[2] and the index of the minimum in A[0..1]
        Repeat this for all the length of the array to win the prize.
        
"""

def best_diff_iterative(A):
    if len(A) >=2:
        
        # init with first two elements
        i = 0
        j = 1
        best_sol = A[j]- A[i]
        
        # save minimum element
        elem_min = min(A[i], A[j])         
        
        # look in the rest of the array
        for index in range(2, len(A)):          
            
            current_sol = A[index] - elem_min
            
            # compare solutions, in case update solution and indexes
            if current_sol > best_sol:
                best_sol = current_sol
                i = A.index(elem_min)
                j = index
                
            # always update minimum element
            elem_min = min(elem_min, A[index])
            
        return (i,j)
    else:
        print("Bad array")

        
def best_diff_recursive(A):
    if len(A) < 2:
        print("Bad array")
    
    if len(A) == 2:
        return (0,1)
    
    if len(A) > 2:
        # solution in A[0..n-1]
        (i,j) = best_diff_rec(A[:-1]) # 2 indexes
        sol_previous = A[j] - A[i]
        
        # solution with indexes of A[n], min(A[0..n-1])
        s = len(A)-1
        r = A.index(min(A[:-1])) 
        sol_current = A[s] - A[r]

        if sol_previous > sol_current:
            return (i,j)
        else:
            return (r,s)