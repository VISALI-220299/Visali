v=input()
k=input()
import sys
if len(v)>len(k):
  print(1)
  sys.exit(0)
A=[]
s=''
for i in range(len(v)):
  if v[i] not in A:
    s+=v[i]
    A.append(v[i])
c=0
c=len(v)//len(s)
d=1
for i in range(2,c+1):
  if c%i==0:
    d+=1
print(d)
