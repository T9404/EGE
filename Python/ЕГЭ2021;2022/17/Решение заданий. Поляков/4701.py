f = open('17-243.txt')

a = [int(x) for x in f.readlines()]

m17 = max(i for i in a if i % 107 == 0) #1 условие
k = 0
m = float('inf')

def f7(x): #2 условие 
    x_7 = ''
    
    while x:
        x_7 += str(x % 7)
        x //= 7
        
    x_7 = x_7[::-1]
    return ('36' in x_7)

for i in range(1, len(a)):
    if max(a[i-1], a[i]) > m17:
        bools = [ f7(a[i-1]), f7(a[i]) ]
        if (True in bools):
            
            k+=1
            m = min(m, a[i]+a[i-1])

print(k, m)

