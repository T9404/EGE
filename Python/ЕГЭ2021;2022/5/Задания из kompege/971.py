def f(x):
    d = [int(x[0]), int(x[1]), int(x[2]), int(x[3])]
    result = str(d[2]*d[3]) + str(d[0] * d[1])

    return int(result)


for i in range(1000, 10000):
    if f(str(i)) == 1214:
        answer = i
print(answer)
