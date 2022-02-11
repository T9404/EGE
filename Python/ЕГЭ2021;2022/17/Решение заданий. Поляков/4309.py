f = open('17.txt')
d = []
while True: 
    x = f.readline()
    if not x: # нету x, тогда пока
        break
    else:
        d.append(x) #ок, берем его
        
k, mik = 0, float('inf')

for i in range(1, len(d)-2): # с 0, 1 и 2, 3го элементов начало
    
    a = int(d[i-1]); b = int(d[i]); c = int(d[i+1]); e = int(d[i+2]) # a, b, c, e будут с теми же знаками!

    if (a > b > c > e):
        if (abs(a-e) > 1000):
            mik = min(a+b+c+e, mik)
            k+=1
    
print(k, mik)
