v,k=map(int,input().split())
lt=[]
cost=0
for i in range(v):
    lt.append(input())
for i in range(v):
    for j in range(k-1):
        if lt[i][j]=="R" and lt[i][j+1]=="R":
            cost=cost+5
        elif lt[i][j]=="G" and lt[i][j+1]=="G":
            cost=cost+3
print(cost)
