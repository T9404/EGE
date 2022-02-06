def f(x):
    d = []
    sq = int(x**0.5)

    for i in range(2, sq+1):
        if x % i == 0:
            d.append(i)
            d.append(x//i)

    if len(d) != 0:
        return abs(max(d)-min(d))
    elif len(d) == 0:
        return 0


number, i = 350000, 1

while i <= 6:
    number += 1
    
    if (f(number) % 23 == 9):
        print(number, f(number))
        i += 1
