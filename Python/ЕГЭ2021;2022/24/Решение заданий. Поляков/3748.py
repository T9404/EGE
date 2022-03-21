f = open('24-157.txt')
s = f.readline()

d = [0]*26

for i in range(len(s)-2):
    if s[i] == s[i+1]:
        d[ord(s[i+2])-ord('A')] += 1


let, mak = 0, 0

for i in range(len(d)):
    if d[i] > mak:
        mak = d[i]
        let = i

print(chr(let+ord('A')) + str(mak))
