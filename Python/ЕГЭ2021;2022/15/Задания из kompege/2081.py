'''
Пусть P – множество всех 8-битовых цепочек, начинающихся с 11,  
Q – множество всех 8-битовых цепочек, оканчивающихся на 0, а 
A – некоторое множество произвольных 8-битовых цепочек. 
Сколько элементов содержит минимальное множество A, при котором для 
любой 8-битовой цепочки x истинно выражение

¬(x∈A) → ((x∈P) ∨ ¬(x∈Q))
'''
# https://prnt.sc/gsdKN5dOHdJT


from itertools import product


P = set(['11'+''.join(x) for x in product('01', repeat=6)])
Q = set([''.join(x)+'0' for x in product('01', repeat=7)])


def f(x, a):
    return (x not in a) <= ((x in P) or (x not in Q))


a = set()


for x in product('01', repeat=8):
    if not f(''.join(x), a):
        a.add(''.join(x))
        

print(len(a))
