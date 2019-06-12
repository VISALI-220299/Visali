v=int(input())
x1=list(map(int,input().split()))
y1=[]
z1=[]
for i1 in range(len(x1)):# for loop starts
    if(i1%2==0):
        y1.append(x1[i1])
    else:
        y1.append(x1[i1])# for loop ends
for j1 in y1:
    d1=sum(y1)
for k1 in z1:
    f1=sum(z1)
if(d1>f1):
    print(d1)
else:
    print(f1)
