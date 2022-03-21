k, df = 0, 0


for a in range(1, 5000+1):
    for b in range(1, 5000+1):

        c = (a * a + b * b)**0.5
        if int(c) == c:
            if (a <= b <= c) and (c <= 5000):
                k += 1

                if (a + b + c) > df:
                    mak = int(c)
                    df = a + b + int(c)
     
                    
print(k, mak)
