g=int(input())

o=int(input())

li=[]

a=[]

for i in range(0,g):
	
	li.append(int(input()))

	for i in range(0,o):
	
	m=0
	
	s=int(input())
	
	p=int(input())
	
	for i in range(s-1,p):
		
		m=m^li[i]
	
	a.append(m)

print(a)
