a=int(input())
print("0" if a>0 and (a & (a-1))==0 else "1")
