f = open('24 (6).txt')

s = f.readline()
s = s.replace('D', ' ')


mik = float('inf')

for i in s.split():
    mik = min(len(i)+2, mik)  # +2 , т.к. граничные входят

print(mik)
