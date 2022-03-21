def F(s, e):
    if s == e:
        return 1
    if s > e:
        return 0
    if s < e:
        return F(s+1, e)+F(s+2, e)


print(F(5, 10)*F(10, 15))
