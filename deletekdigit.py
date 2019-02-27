k=list(input())
v=list(input())
m=len(k)
s=len(v)
i=0
j=0
c=[]
while m>0:
    if k[i]==v[j]:
        c.append(k[i])
    j=j+1
    i=i+1
    m=m-1
print(s-len(c))
