num1=int(input())
arr1=list()
for x in range(num1):
	arr2=list(map(int,input().split()))
	arr1=arr1+arr2
arr1=sorted(arr1)
for s in arr1:
	print(s,end=" ")
