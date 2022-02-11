def f(n):
    k = n*n
    if n > 1:
        k += ( (2*n+1) + f(n-2) + f(n//3) )
        
    return k

print(f(100))

        
    
