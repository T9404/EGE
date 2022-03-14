for t in 'ab':
    with open(f'27-86{t}.txt') as f:
        N, K = map(int, f.readline().split())

        m = 0
        s = {0: (0, 0)}
        for i in range(N):
            x = int(f.readline())
            rfux = x < 0 and str(x)[-1] == '7'
            c = [(sm + x, cs + rfux) for sm, cs in s.values()] + [(x, rfux)]
            s = {x[1]%K: x for x in sorted(c)}
            m = max(m, s.get(0, (0, 0))[0])

        print(m)
