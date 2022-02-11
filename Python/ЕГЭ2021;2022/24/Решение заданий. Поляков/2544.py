f = open('24-j5.txt')
s = f.readline()


while 'STOCK' in s:
    s = s.replace('STOCK', '', 1)
    
print(s.count('OCK'))
