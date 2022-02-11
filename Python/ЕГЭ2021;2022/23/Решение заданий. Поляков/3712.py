def F(s,e):
    if s==e:
        return 1
    if s<e:
        return 0
    else:
        return F(s-1,e)+F(int(bin(s)[2:][0:len(bin(s)[2:])-1],2),e)


print(F(int('110111',2),int('110',2)))

