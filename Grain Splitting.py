'''
# your code goes here
#2 1 1 4 3 3 
# 1 1 2 3 3 4
# 1 1 2 3
# 3 4
def grain(arr):
	left=-1
	right=len(arr)
	sumleft=0
	sumright=0
	while left<right:
		if sumleft==sumright and left+1==right:
			return right
		if sumleft>sumright:
			right-=1
			sumright+=arr[right]
		elif sumright>=sumleft:
			left+=1
			sumleft+=arr[left]
	return right
t=int(input())
print(t)
for i in range(t):
	arr=[int(x) for x in input().split()]
	arr.sort()
	index=grain(arr)
	for i in range(index,len(arr)):
		print(arr[i],end=" ")
'''
# your code goes here
#2 1 1 4 3 3 
# 1 1 2 3 3 4
# 1 1 2 3
# 3 4
def grain(arr):
	left=-1
	right=len(arr)
	sumleft=0
	sumright=0
	while left<right:
		if sumleft==sumright and left+1==right:
			return right
		if sumleft>sumright:
			right-=1
			sumright+=arr[right]
		elif sumright>=sumleft:
			left+=1
			sumleft+=arr[left]
	return right
t=int(input())
print(t)
for i in range(t):
	arr=[int(x) for x in input().split()]
	arr.sort()
	index=grain(arr)
	for i in range(index,len(arr)):
		print(arr[i],end=" ")