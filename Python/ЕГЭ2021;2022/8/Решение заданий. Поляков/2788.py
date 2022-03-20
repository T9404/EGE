from itertools import product


count = 0

for x in product('1234', repeat=5):
    s = ''.join(x)
    if (s[0] != '1') and (s != s[::-1]):
        count += 1

print(count)
