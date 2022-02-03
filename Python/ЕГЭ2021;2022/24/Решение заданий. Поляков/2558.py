f = open('24-s1.txt')


count = 0

while True:
    s = f.readline()

    if not s:
        break

    for i in range(1, len(s)-1):
        if s[i-1] == 'A' and s[i+1] == 'R':
            count += 1
            break

print(count)
