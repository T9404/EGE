start = int('1000', 8)
stop = int('10000', 8)
a = [i for i in range(start, stop) if (i % 4 == 0 and len(oct(i)[2:]) == 4) ]
print(len(a))

