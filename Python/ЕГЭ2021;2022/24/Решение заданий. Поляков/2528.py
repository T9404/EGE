f = open('C:\\Users\\XiaoMai\\Downloads\\24-1 (1).txt')
s = str(f.readline())


def F(n):
    for i in range(len(n)):
        if (int(n[i]) % 2 == 1):
            return False
    else:
        return True


for i in range(ord('A'), ord('Z')+1):
    s = s.replace(chr(i), ' ', s.count(chr(i)))

print(max(int(x) for x in s.split() if (F(x) == True)))
