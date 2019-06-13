string=input()
flag3=0
for i in range(0,len(string)-1):
  for j in range(i+1,len(string)):
    if string[i]<string[j]:
      flag3=1
      print(string[j:])
      break
  if flag3==1:
    break
else:
  print(string)
