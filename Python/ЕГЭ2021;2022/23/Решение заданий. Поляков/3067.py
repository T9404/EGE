def F(s, e):
    if s == e:
        return 1
    if s > e:
        return 0
    if s < e:
        return F(s+1, e)+F(s+2, e)+F(s+s-1, e)


print(F(3, 10))
