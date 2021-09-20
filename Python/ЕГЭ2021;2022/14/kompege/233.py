c = 3 * 16 ** 8 - 4 ** 5 + 3
c_4 = ''

while c:
    c_4 += str(c % 4)
    c //= 4
    
print(c_4.count('3'))
