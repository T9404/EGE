f = open('24-211.txt')
s = f.readline()


elements = ['ABEC', 'BDAC', 'CAFB', 'CFBA']
mak = float('-inf')


for i in range(3, len(s)):
    if s[i-3:i+1] in elements:
        j = i + 3
        k = 1

        while j < len(s):
            if s[j-3:j+1] in elements:
                k += 1
                j += 3
            else:
                break

        mak = max(mak, k)


print(mak)
