p = [ i for i in range(35, 55+1) ]
q = [ i for i in range(45, 65+1) ]

a = set()
def f(x, a):
    return (( x in p) <= (x in a))  and ((x not in a) <= (x not in q) )

for x in [i for i in range(1, 1000) ]:
    if not f(x, a):
        a.add(x)
print(len(a)-1) # не количество, а длина
#print(a)
