def F(s, e):
    if s == e:
        return 1
    if s < e:
        return 0
    else:
        if (s > 4):
            return F(s-1, e)+F(s-3, e)+F(s % 4, e)
        else:
            return F(s-1, e)+F(s-3, e)


print(F(22, 2))
