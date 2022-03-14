for t in 'ab':
    with open(f'27-60{t}.txt') as f:
        N = int(f.readline())

        s = {0: 0}
        for i in range(N):
            x = int(f.readline())
            c = [sm + x for sm in s.values()] + [x] + list(s.values())
            s = {x%25: x for x in sorted(c)}

        print(s[0])
    
