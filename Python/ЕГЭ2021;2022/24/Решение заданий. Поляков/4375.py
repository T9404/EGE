f = open('24-178.txt')
s = f.readline()[:-1] # убираем '\n' 
s += s

answer = 0

for i in range(len(s)):
    string_, start = s[i],  s[i]
    j = i + 1

    while j < len(s):
        if ord(s[j]) >= ord(start):
            start = s[j]
            string_ += s[j]
            j += 1
        else:
            answer = max(answer, len(string_))
            break
       
print(answer)
