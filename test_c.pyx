#cython
def sum_cy(long long n):
    cdef long long i = 0, j
     
    for j in range(n + 1):
        i  = i + j
    
    return i
