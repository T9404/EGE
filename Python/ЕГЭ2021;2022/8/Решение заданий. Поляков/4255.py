#1 решение
start = int('1000', 8)
stop = int('10000', 8)
a = [i for i in range(start, stop) if (i % 4 == 0 and len(oct(i)[2:]) == 4) ]
print(len(a))

#2 решение
k = 0
for i in range(1, 10000):
    if i % 4 == 0 and (len(str(oct(i))[2:]) == 4):
            k+=1
print(k)







