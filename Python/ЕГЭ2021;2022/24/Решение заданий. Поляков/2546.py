f = open('24-j5.txt')
s = f.readline()


mak, k, i = 0, 0, 1

while True:
    try:
        if s[i-1] == 'K' and s[i] == 'O' and s[i+1] == 'T':
            k += 1
            i += 3
        else:
            mak = max(mak, k)
            k = 0
            i += 1
    except:
        break

print(mak)
