'''
# your code goes here
def modifiedpalidrome(st):
	mismatch=0
	i,j=0,len(st)-1
	flag1=True
	while i<j:
		if st[i]!=st[j]:
			mismatch+=1
			if mismatch <=1:
				i+=1 #try delete ith
			else:
				flag1=False
				break
		else:
			i+=1
			j-=1
	mismatch=0
	flag2=True
	while i<j:
		if st[i]!=st[j]:
			mismatch+=1
			if mismatch<=1:
				j-=1 #try delete jth
			else:
				flag2=False
				break
		else:
			i+=1
	return (flag1 or flag2)

for i in range(int(input())):
	s=input()
	print(modifiedpalidrome(s))
			
'''
# your code goes here
def modifiedpalidrome(st):
	mismatch=0
	i,j=0,len(st)-1
	flag1=True
	while i<j:
		if st[i]!=st[j]:
			mismatch+=1
			if mismatch <=1:
				i+=1 #try delete ith
			else:
				flag1=False
				break
		else:
			i+=1
			j-=1
	mismatch=0
	flag2=True
	while i<j:
		if st[i]!=st[j]:
			mismatch+=1
			if mismatch<=1:
				j-=1 #try delete jth
			else:
				flag2=False
				break
		else:
			i+=1
	return (flag1 or flag2)

for i in range(int(input())):
	s=input()
	print(modifiedpalidrome(s))
			