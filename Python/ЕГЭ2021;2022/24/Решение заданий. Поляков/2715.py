f = open('C:\\Users\\XiaoMai\\Downloads\\24-j7.txt')
s = f.readline()

max_length, length = 0, 1

for i in range(0, len(s)-1):
    if (int(s[i]) % 2 == int(s[i+1]) % 2):
        length += 1
        max_length = max(max_length, length)
    else:
        length = 1

print(max_length)
