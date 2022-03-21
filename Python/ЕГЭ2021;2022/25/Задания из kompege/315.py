def f(x):
    d = set()

    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)

    return d


for x in range(326496, 649632+1):
    arr = f(x)
    if arr:
        chet = [i for i in arr if i % 2 == 0]
        nechet = [i for i in arr if i % 2 != 0]
        
        if len(chet) == len(nechet) and len(chet) > 70:
            answer = [i for i in arr if i > 1000]
            print(x, min(answer))
