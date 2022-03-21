f = open('24-197.txt')
s = f.readline()


answer = 0


for i in range(len(s)-2):

    if s[i:i+3] in ['ZXY', 'ZYX']:
        k = 1
        j = i + 3

        while j + 2 <= len(s):

            if s[j:j+3] in ['ZXY', 'ZYX']:
                k += 1
                j += 3

            else:
                answer = max(answer, k)
                break


print(answer)
