a=int(input())
b=int(input())
for i in range(a,b+1):
	s=0
	t=i
	while(t>0):
		d=t%10
		s=s+d**3
		t=t//10
		if(i==s):
			print(i)
