for t in 'ab':
    with open(f'27-72{t}.txt') as f:
        N = int(f.readline())

        count, s = 0, 0
        k = {x: 0 for x in range(71)}
        for i in range(N):
            s += int(f.readline())
            count += k[s%71] + (s%71 == 0)
            k[s%71] += 1

        print(count)
