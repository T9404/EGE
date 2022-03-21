def f(x, i):
    x_i = ''

    while x:
        x_i += str(x % i)
        x //= i 
    
    return sum(map(int, x_i[::-1]))


mak = 0


for j in range(2, 10+1):
    if mak < f(2345, j):
        mak = f(2345, j)
        ans = j


print(ans)    
