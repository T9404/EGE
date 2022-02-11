def find_dev(n):
    a = [ (i, n//i) for i in range(2, int(n**0.5)+1) if n % i == 0]
    ans = float('inf')
    for i in a:
        if i[0] % 10 == 8 and i[0] != 8 and i != n: 
            ans = min(ans, i[0])
        if i[1] % 10 == 8 and i[1] != 8 and i != n:
            ans = min(ans, i[1])
    if ans != float('inf'):
        return ans
    else:
        return False


i = 500_000
k = 0
while k < 5:
    i += 1
    if find_dev(i):
        k += 1
        print(i, find_dev(i))
    
