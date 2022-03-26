from itertools import product


def check(m):
    arr = list(m)

    for i in range(len(arr)-1):
        if arr[i+1] == arr[i]:
            return False

    return True


k = 0


for r in range(3, 9+1):
    for i in product('0123456', repeat=r):
        w = ''.join(i)
        
        if check(w):
            k += 1


print(k)
