from itertools import permutations
l = 0
for x in set(permutations('ДЕЙКСТРА', r=6)):
    s = ''.join(x)
    if s.count('Й') == 1:
        if ('ЙД' in s) or ('ЙК' in s) or ('ЙС' in s) or ('ЙТ' in s) or 'ЙР' in s:
            l+=1
print(l)
    
