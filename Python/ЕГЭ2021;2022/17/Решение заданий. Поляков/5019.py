f = open('17-278.txt')


a = [int(x) for x in f.readlines()]


num = sum([(oct(abs(i))[2:].count('7') * 7) for i in a])


k, mini = 0, float('inf')


for i in range(len(a)-1):
    if a[i] > num and a[i+1] > num:
        k += 1
        mini = min(mini, a[i]+a[i+1])


print(k, mini)
