k=input()
v=input()
m=list(str(k))
s=v
while s>0:
    s=s-1
    del(m[s])
print(''.join(m))
