min_numb = float('inf')


for i in range(101, 120):
    s = '3' * i

    while '111' in s or '333' in s:
        if '111' in s:
            s = s.replace('111', '3', 1)
        else:
            s = s.replace('333', '1', 1)

    if min_numb > sum(map(int, s)):
        min_numb = sum(map(int, s))
        j = i


print(j)
