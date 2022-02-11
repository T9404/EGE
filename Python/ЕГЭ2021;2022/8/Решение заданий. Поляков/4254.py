from itertools import product


k = 0

for s in set(product('01234', repeat=5)):
    num = ''.join(s)
    if (num.count('0') + num.count('2') + num.count('4')) <= 3 and num[0] != '0':
        k += 1  # число с нуля не начинается

print(k)
