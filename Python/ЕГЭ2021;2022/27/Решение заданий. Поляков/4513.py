for t in 'ab':
    with open(f'27-80{t}.txt') as f:
        N = int(f.readline())

        m = 0
        s = {0: (0, 0)}
        for i in range(N):
            x = int(f.readline())
            c = [(sm + x, cs + (x%5 == 0)) for sm, cs in s.values()] + [(x, (x%5 == 0))]
            s = {x[1]%3: x for x in sorted(c)}
            m = max(m, s.get(0, (0, 0))[0])
            
        print(m)
            
    
