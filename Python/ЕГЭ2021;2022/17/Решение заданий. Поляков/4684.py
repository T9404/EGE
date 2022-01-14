f = open('17-1.txt')
a = [ int(x) for x in f.readlines() ]

middle = sum(a) / len(a)
k = maxx = 0

for i in range(len(a)-2):
    d = sorted([ a[i], a[i+1], a[i+2] ])
    if d[0] < middle and d[1] < middle:
        
        ost = [ (abs(d[i]) % 10 == 8) for i in range(3) ] # Берем по модулю(abs), True-False
        if sum(ost) >= 2:
            k += 1
            maxx = max(sum(d), maxx)

print(k, maxx)
            
            
