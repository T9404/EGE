f = open('C:\\Users\\XiaoMai\\Downloads\\24-191.txt')
s = str(f.readline())

s = s.replace('A', 'A A', s.count('A')).replace('B', 'B B', s.count('B'))

print(len([x for x in s.split() if x[0] == 'A' and x[len(x)-1] == 'B' and x.count('F')
      >= 1 and x.count('A') == 1 and x.count('B') == 1 and len(x) <= 15]))
