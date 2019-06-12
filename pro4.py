inv1,inv2=input().split()
temp=0
if len(inv1)>len(inv2):
  inv1,inv2=inv2,inv1
i=0
while i<len(inv1):
  temp+=(ord(inv2[i])-ord(inv1[i]))
  i+=1
for i in range(i,len(inv2)):
  temp+=ord(inv2[i])-ord('a')+1
print(temp)
