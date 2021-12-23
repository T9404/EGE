def S(n):
  a=set()
  for i in range(2,int(n**0.5)+1):
    if (n%i==0):
      a.add(i)
      a.add(n//i)
  k=list(a)
  k.sort(reverse=True)
  if len(k)>=3: return sum(k[0:3])
  else: return 0

def F(n):
  for i in range(2,int(n**0.5)+1):
    if (n%i==0): return False
  else: return True

c=0
for i in range(10**7+1,10**9):
  if (S(i)!=0) and (F(S(i))==True):
    c+=1
    if c<=5:
      print(S(i))
    else: break

