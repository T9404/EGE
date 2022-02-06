def F(n):
    n = str(n)

    if all(int(d) % 2 == 0 for d in [n[0], n[1]]) and all(int(d) % 2 == 1 for d in [n[2], n[3], n[4]]):
        return True
    else:
        return False


a = [x for x in range(64444, 77564) if (F(x) == True)
     and all(x % d != 0 for d in [9, 13, 17])]
     
print(len(a), max(a)-min(a))
