s = 7 ** 2103 - 6 * 7 ** 1270 + 3 * 7 **57 - 98

s_7 = ''

while s:
    s_7 += str(s % 7)
    s //= 7

ans = sum(map(int, s_7))
print(ans)
