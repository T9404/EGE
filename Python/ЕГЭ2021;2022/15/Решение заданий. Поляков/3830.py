print(min([a for a in range(1,100000) if all(((a%7==0)and((240%x==0)<=((a%x!=0)<=(780%x!=0))))==1 for x in range(1,10000))]))
