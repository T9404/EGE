def d(n):
    sum = 0

    for i in range(1, n):
        if (n % i == 0):
            sum += i
            
    return sum


a = [x for x in range(2, 20001) if (x < d(x))]
print(len(a))
