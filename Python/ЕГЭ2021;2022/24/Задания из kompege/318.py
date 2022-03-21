f = open('24.txt')
s = f.readline()


mak = 0

for i in range(len(s)):
    try:
        if s[i] in '123456789':
            j = i + 1
            stik = s[i]

            while s[j] in '0123456789':
                stik += s[j]
                j += 1

            if int(stik) % 2 != 0:
                mak = max(mak, int(stik))
    except:
        break

print(mak)
