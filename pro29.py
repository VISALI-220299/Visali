v=int(input())
i=0
x=0
b=[]
while i<90 and i<v:
  r=0
  for j in str(v-i):
    r+=int(j)
  if r+(v-i)==v:
    x+=1
    b.append(v-i)
  i+=1
print(x)
for i in b:
  print(i)
