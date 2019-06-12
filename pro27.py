a,k=map(int,input().split())
b=list(map(int,input().split()))
v=list(map(int,input().split()))
t=[]
c=0
for i in range(a):
    x=v[i]/b[i]
    t.append(x)
while k>=0 and len(t)>0:
    mindex=t.index(max(t))
    if k>=b[mindex]:
        c=c+v[mindex]
        k=k-b[mindex]
    b.pop(mindex)
    v.pop(mindex)
    t.pop(mindex)
print(c)
