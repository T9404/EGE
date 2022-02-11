def f(x, a):
    return (a % 5 == 0) and (not(2020 % a == 0) <= (x % 1718 == 0) <= (2023 % a == 0)) 

k = 0
for a in range(1, 100000):
    if all( f(x, a) == 1 for x in range(1, 100)):
        k+=1

print(k)
