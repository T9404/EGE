f = open('26 (2).txt')
n = int(f.readline())

values = sorted([int(x) for x in f.readlines()])

k = 0
ans = float('inf')

for i in range(len(values)-1):
    for j in range(i+1, len(values)):
        sumx = ( values[i]+values[j] )
        if ( sumx % 2 == 0 ):  
            sumx //= 2 
            if ( values[ (len(values)//2) - 1] < sumx ) and (values[(len(values))//4*3] > sumx):
                k += 1
                ans = min(ans, sumx)

print(k, ans)
