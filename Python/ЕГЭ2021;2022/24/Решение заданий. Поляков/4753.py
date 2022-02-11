f = open('24-181.txt')
s = f.readline()

letters = ['A', 'E', 'I', 'O', 'U', 'Y']
for i in letters:
    s = s.replace(i, ' ')
    
mak = 0
for w in s.split():
    if w.count('.') >= 6:
        mak = max(mak, len(w))
        
print(mak)

