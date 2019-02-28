k=int(input())
v=int(input())
li=[]
a=[]
for i in range(0,k):
		li.append(int(input()))
		for i in range(0,v):
			m=0
			s=int(input())
			p=int(input())
		for i in range(s-1,p):
			m=m^li[i]
			a.append(m)
print(a)
