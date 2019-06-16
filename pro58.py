num = int(input())
b = []
a = num//2 + num
for i in range(1,num+1):
  if i%2==0:
    b.append(i)
for i in range(1,num+1):
  if i%2!=0:
    b.append(i)
for i in range(1,num+1):
  if i%2==0:
    b.append(i)
print(a)
print(*b)
