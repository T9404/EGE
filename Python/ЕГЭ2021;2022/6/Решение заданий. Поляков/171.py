''' 
При каком наибольшем введенном числе d после выполнения программы будет напечатано 55?
'''
# https://prnt.sc/lcZAlqXnJ3Sb


for i in reversed(range(10**6)):
    d = i
    s, n = 0, 0
    
    while s <= 365:
        s += d
        n += 5
        
    if n == 55:
        print(i)
        break
