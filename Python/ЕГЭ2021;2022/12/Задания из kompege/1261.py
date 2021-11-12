s = '112' * 4 +'1'* (12-8) 

# 4 => 7
# 2 => 3

#очевидно, что выгоднее 4 => 7 , т.е. (112->7)

while '11' in s:
    if '112' in s:
        s = s.replace('112', '7', 1)
    else:
        s = s.replace('11', '3', 1)

print(sum(map(int, s)))

