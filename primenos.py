l=int(input())
u=int(input())
for v in range(l,u+1):
   if v > 1:
       for i in range(2,v):
           if (v % i) == 0:
               break
       else:
           print(v)
