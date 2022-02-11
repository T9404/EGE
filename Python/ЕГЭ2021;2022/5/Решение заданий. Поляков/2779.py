n = 120

a = '0'*(8-len(bin(n)[2:]))+bin(n)[2:]
l = ''

for i in range(8):
    l+=str(1-int(a[i]))
    
l = bin(int(l, 2)+1)[2:]

print(int(l, 2))
