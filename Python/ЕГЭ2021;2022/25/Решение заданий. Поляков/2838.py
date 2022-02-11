def F(n):
    s = set()
    c = 0

    for i in range(2, int(n**0.5)+1):
        if (n % i == 0):
            if (i % 2 == 0) or ((n//i) % 2 == 0):
                c += 1

            if (i % 2 == 1):
                s.add(i)
                
            if ((n//i) % 2 == 1):
                s.add(n//i)

    if (c == 0):
        return s
    else:
        return [0]


for i in range(321654, 654322):
    if (len(F(i)) > 70):
        print(i, max(F(i)))
