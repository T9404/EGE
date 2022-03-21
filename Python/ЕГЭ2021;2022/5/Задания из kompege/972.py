def f(x):
    d = [int(x[0]), int(x[1]), int(x[2])]
    result = str(d[0]*d[1]) + str(d[1] * d[2])

    return int(result)


for i in range(100, 1000):
    if f(str(i)) == 240:
        answer = i

print(answer)
