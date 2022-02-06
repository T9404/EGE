f = open('24-s1.txt')


answer = 0

while True:
    s = f.readline()
    
    if not s:
        break

    if s.count('YZ') > 1:
        answer += 1

print(answer)
