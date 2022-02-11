f = open('C:\\Users\\XiaoMai\\Downloads\\24-173.txt')
s = str(f.readline())


max_len, l = 0, 0

for i in range(0, len(s)-5):
    if s[i:i+3] != s[i+3:i+6]:
        l += 1
    else:
        max_len = max(l+5, max_len)
        l = 0

print(max_len)
