num=int(input())
v=[]
k=bin(2**num-1)[2::]
l=len(k)
for i in range(0,2**num):
	s=bin(i)[2::]
	if len(s)<l:
		v.append([s.count("1"),(l-len(s))*"0"+s])
	else:
		v.append([s.count("1"),s])
v.sort()
for i in range(0,len(v)):
	print(v[i][1])
