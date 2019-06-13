s,p,q,r=map(int,input().split())
v=[int(i) for i in input().split()]
c=[p*v[i]+q*v[j]+r*v[k] for i in range(len(v)) for j in range(len(v)) for k in range(len(v)) if i<=j<=k]
print(max(c))
