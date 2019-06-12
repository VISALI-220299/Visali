c,b=map(int,input().split())
r=list(map(int,input().split()))
s=0
y=sorted(r)
x=(y[::-1])
for i in range(0,len(x)):
    a = b //(x[i])
    s = s + a
    b = b - (a *x[i])
print(s)
