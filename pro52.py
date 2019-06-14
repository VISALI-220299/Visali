value1,value2=map(int,input().split())
value3,value4=map(int,input().split())
value5,value6=map(int,input().split())
value7,value8=map(int,input().split())
t1=value4-value2
t2=value6-value8
t3=value5-value3
t4=value7-value1
if t1==t2==t3==t4:
  print("yes")
else:
  print("no")
