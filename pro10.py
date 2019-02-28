def stair():
	k=0
	v=[]
	n=int(input())
	for i in range(n):
		v.append(int(input()))
	for i in v:
		k+=(n-i)
	print(k)
  
try:
  stair()
except:
  print('invalid')
  p
