from modul import *
start = 3532000
end = 3532160
n=0

for x in range(start, end + 1):
    if isPrime(x):
        n+=1
        print(n, x)