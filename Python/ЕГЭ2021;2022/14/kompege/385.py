k = 0
for x in range(1, 10000):
    if x < int('10000', 5):
        if x > int('10000', 2):
            if x % 16 == 12:
                k+=1
print(k)
