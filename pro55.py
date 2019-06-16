num,k = map(int,input().split())
v = list(map(int,input().split()))
b,c = 0,[]
for i in range(0,len(v)):
  t = i
  for p in range(0,len(v)):
    for l in range(0,k):
      if l == k-1:
        try:
          b += v[p+i]
        except IndexError:
            t = t-1
            b +=v[t]
      else:
        b += v[i]
    c.append(b)
    b = 0
for i in range(0,len(v),k):
  b = sum(a[i:i+k])
  c.append(b)
print(*sorted(set(c)))
