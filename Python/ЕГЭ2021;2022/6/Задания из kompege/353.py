s = []

for i in range(1, 10000):
    d = i
    n = 1
    while d // n > 0:
        d -= 2
        n += 3
    if n == 46:
        s.append(i)
        
print(min(s)+max(s))
