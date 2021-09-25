f = open('24-153.txt')
s = f.readline()
mik = float('inf')

for i in range(len(s)):
    if s[i] == 'D':
        z = 'D'
        j = i + 1
        try:
            while s[j] != 'D':
                z += s[j]
                j+=1
            z += 'D'
            if len(z) != 2:
                mik = min(len(z), mik)
        except:
            continue
        
print(mik)
        
