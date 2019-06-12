v,b=map(int,input().split())
if v<=b:
  d=v
else:
  d=b
m=[]
for i in range(0,d):
  m.append(sorted(list(map(int,input().split()))))
m=sorted(m)
for i in range(0,len(m[0])):
  for j in range(0,len(m)-1):
    if m[j][i]>m[j+1][i]:
      m[j][i],m[j+1][i]=m[j+1][i],m[j][i]
for i in m:
  print(*i)
