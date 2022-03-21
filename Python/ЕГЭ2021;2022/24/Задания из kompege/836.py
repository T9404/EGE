f = open('24_2.txt')
s = f.readline()


k = 0

for i in range(2, len(s)-2):
    if s[i-2:i] == s[i+1:i+3][::-1]:
        k += 1
        
print(k)
