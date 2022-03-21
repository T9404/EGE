f = open('C:\\Users\\XiaoMai\\Downloads\\24-s1.txt')


all_f, our_len = '', ''
max_q = 0


for s in f:
    all_f += s
    if (s.count('Q') > max_q):
        max_q = s.count('Q')
        our_len = s


min_count = float('inf')
min_c = ''


for a in range(ord('A'), ord('Z')+1):
    q = chr(a)
    c = 0

    for i in range(len(our_len)):
        if (our_len[i] == q):
            c += 1
            
    if (c < min_count) and (c != 0):
        min_c = q
        min_count = c


print(min_c, all_f.count(min_c))
