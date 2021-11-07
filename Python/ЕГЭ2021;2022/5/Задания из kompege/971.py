def f(x):
    if  10000 > x > 999:
        x = str(x)
        d = [ int(x[0]), int(x[1]), int(x[2]), int(x[3]) ]
        result = str(d[2]*d[3]) + str(d[0] * d[1])
        return int(result)
    else:
        return None

#print(f(5431))

for i in range(1000, 9999):
    if f(i) == 1214:
        answer = i
print(answer)
