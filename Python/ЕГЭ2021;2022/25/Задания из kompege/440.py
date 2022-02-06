def f(x):
    d = set()

    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)

    return d


for x in range(321654, 654321+1):
    arr = f(x)
    nechet = [i for i in arr if i % 2 != 0]
    
    if len(nechet) > 70 and len(arr) == len(nechet):
        print(x, max(arr))
