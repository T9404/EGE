f = open('24-153.txt')
s = f.readline() + 'B'*100


mina = float('inf')
for i in range(len(s)):
    if s[i] == 'A':
        l = 1
        j = i + 1

        while s[j] != 'F':
            l += 1
            j += 1

        l += 1
        if (l != 2) and (l != 1):
            mina = min(mina, l)

print(mina)
