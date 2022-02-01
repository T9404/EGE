s = '2' + '5' * 81

while '25' in s or '355' in s or '4555' in s:
    if '25' in s:
        s = s.replace('25', '4', 1)
    if '355' in s:
        s = s.replace('355', '2', 1)
    if '4555' in s:
        s = s.replace('4555', '3', 1)

print(s)
