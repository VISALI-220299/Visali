v=int(input())
k=list(map(int,input().split()))
k.sort()
s=0
c=0
for i in range(len(k)):
    if k[i]>=s:
        c=c+1
    s=s+k[i]
print(c)
