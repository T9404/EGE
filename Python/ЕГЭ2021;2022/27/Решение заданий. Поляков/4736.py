for t in 'ab':
    with open(f'27-84{t}.txt') as f:
        N, K = map(int, f.readline().split())

        r = (0, 0)
        s = {0: 0}
        for i in range(N):
            x = int(f.readline())
            c = [[x + y, 1 + s[y]] for y in s.keys()]
            for sm, ln in c:
                if sm <= K and (sm not in s or ln > s[sm]):
                    s[sm] = ln
                
        for sm, ln in s.items():
            if (abs(K - sm) < abs(K - r[0])) or ((abs(K - sm) == abs(K - r[0])) and ln > r[1]):
                r = (sm, ln)

    print(r[1])
