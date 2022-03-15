f = open('17-7.txt')
a = [int(x) for x in f.readlines()]


b = [i for i in a if (i % 256 != 109 and i % 16 == 9)]
print(len(b), max(b))
