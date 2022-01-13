f = open('24 (6).txt')
s = f.readlines()
k = 0
for i in s:
    if i.count('S') == i.count('X'):
        k+=1
print(k)
