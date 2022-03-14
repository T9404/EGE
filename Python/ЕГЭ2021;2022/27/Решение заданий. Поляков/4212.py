for t in 'ab':
    with open(f'27-71{t}.txt') as f:
        N = int(f.readline())

        k = {x: (10**30, 0) for x in range(69)}
        s, m, l = 0, 0, 0
        for i in range(N):
            s += int(f.readline())
            if s - k[s%69][0] > m or (s - k[s%69][0] == m and \
            i + 1 - k[s%69][1] < l):
                m, l = s - k[s%69][0], i + 1 - k[s%69][1]
            if s < k[s%69][0]:
                k[s%69] = (s, i + 1)

        print(l)
            
