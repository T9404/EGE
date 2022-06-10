f = open('24.txt')
s = f.readline()


mak = float('-inf')


for i in range(1, len(s)-1):
    if s[i] != s[i-1] and s[i] != s[i+1]:
        j = i + 1
        count = 1

        while j < len(s) - 1:  # не берем последний элемент
            if s[j] != s[j-1] and s[j] != s[j+1]:
                count += 1
                j += 1
            else:
                mak = max(count, mak)
                break


print(mak)
