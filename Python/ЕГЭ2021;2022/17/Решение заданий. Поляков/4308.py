f = open('17.txt')


d = [int(x) for x in f.readlines()]


k, mik = 0, 0


for i in range(1, len(d)-2):  # с 0, 1 и 2, 3го элементов начало

    a = int(d[i-1])
    b = int(d[i])
    c = int(d[i+1])
    e = int(d[i+2])  # a, b, c, e будут с теми же знаками!

    if (abs(a) % 2 != abs(b) % 2):

        if (abs(b) % 2 != (abs(c) % 2)):

            if (abs(c) % 2 != abs(e) % 2):
                mik = max(a+b+c+e, mik)
                k += 1


print(k, mik)
