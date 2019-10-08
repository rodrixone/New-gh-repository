a = 5
for i in range(a):
	print(i)
v=[0]*a
v[0],v[1]=-1,1
for i in range(2,a):
	v[i]=v[i-1]+v[i-2]
a=0
