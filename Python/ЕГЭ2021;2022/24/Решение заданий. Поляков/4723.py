f = open('24-186.txt')
s = f.readline()


k = 0

for i in range(len(s)-11):
    try:
        if s[i] == '7' and ((int(s[i])+int(s[i+1]))) == ((int(s[i+9]) + int(s[i+10]))):
            k += 1
    except:
        continue

print(k)
