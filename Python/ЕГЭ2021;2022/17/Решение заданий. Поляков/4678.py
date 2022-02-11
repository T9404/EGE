f = open('17-1.txt')

a = [ int(x) for x in f.readlines()]
m = amount = 0
average = (sum(a) / len(a)) 

for j in range(1, len(a)-1):
    arr = [ a[j-1], a[j], a[j+1] ]
    
    if min(arr) < average: #1 условие
        k = 0
        for i in arr:
            if '2' in str(i):
                k+=1
        if k >= 2: #2 условие
            amount += 1
            m = max(m, sum(arr))

print(amount, m)
        
                
