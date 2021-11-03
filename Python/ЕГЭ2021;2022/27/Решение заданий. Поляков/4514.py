f = open('27-81bb.txt')
n = int(f.readline())

z = [float('inf')]*13
k = s = answer = 0

for _ in range(n):
    x = int(f.readline())
    s+=x
    
    if x % 2 != 0: k+=1
    if k % 13 == 0:
        answer = s
    elif (z[k % 13] != float('inf')):
        answer = max(answer, s-z[k % 13])

    z[k % 13] = min(z[k % 13], s)
    
print(answer)
