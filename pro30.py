v=input()
flag=0
for i in range(1,len(v)):
  j=0
  while j<len(v) and len(v[:j]+v[i+j:])==len(v)-i:
    n=v[:j]+v[j+i:]
    if int(n)%8==0:
      flag=1
      print('yes')
      break
    j+=1
  if flag==1:
      break
else:
  print('no')
