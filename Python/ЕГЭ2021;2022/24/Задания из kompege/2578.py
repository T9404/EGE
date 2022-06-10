f = open('24.txt')
w = f.readline()


array = w.split('.')
mak = float('-inf')

for s in array:
    for i in range(len(s)):
        m = s[i]
        j = i + 1
        count_vowels = (m.count('A')+m.count('E')+m.count('I') +
                        m.count('O')+m.count('U')+m.count('Y'))

        while j < len(s):
            if (count_vowels == 7) and (s[j] in 'AEIOUY'):
                break
            else:
                m += s[j]
                j += 1

        mak = max(mak, len(m))

print(mak)
