for i in range(1,100000):
    a=bin(i)[2:]
    a+=a[len(a)-1]
    a+=str(a.count('1')%2)
    a+=str(a.count('1')%2)

    r=int(a,2)
    if (r>144):
        print(r)
        break

