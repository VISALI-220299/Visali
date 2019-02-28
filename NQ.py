def hcf(a,b):
	while(b!=0):
		t=b
		b=a%b
		a=t
	return a
def main():
	n=int(input())
	q=int(input())
	(l,r)=([],[])
	for i in range(n):
		l.append(int(input()))
	print(l)
	for c in range(q):
		a=int(input())
		b=int(input())
		r.append(hcf(l[a-1],l[a-1]))
	for i in r:
		print(r)
try:
  main()
except:
  print('invalid')
  p
