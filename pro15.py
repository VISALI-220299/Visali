x=int(input())
y=list(map(int,input().split()))
w=x=[]
for i in range(0,q):
    w=list(bin(y[i]))
    w=w[2:]
    x.append(w)
x=sorted(x)
x=x[::-1]
for i in range(0,q):
    b=1
    z=0
    for j in range(len(x[i])-1,-1,-1):
        z=z+(int(x[i][j])*b)
        b=b*2
    print(z)
