f = open('242.txt')
s = f.readlines()


def check_str(w):
    for i in range(1, len(w)-2):
        if w[i-1] == 'K' and w[i+1:i+3] == 'GE':
            return True
    return False


k = 0

for w in s:
    if check_str(w):
        k += 1

print(k)
