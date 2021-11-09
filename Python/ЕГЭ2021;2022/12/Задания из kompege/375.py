s = '1' + '0' * 33

while '1' in s or '100' in s:
    if '100' in s:
        s = s.replace('100', '0001', 1)
    else:
        s = s.replace('1', '00', 1)

print(s.count('0'))
