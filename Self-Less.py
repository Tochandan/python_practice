'''
Self-Less
Given an array nums of n integers where n > 0, print an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

If the array has only 1 element, print 1 as result.

Note:
Please solve it without division and in O(n).
Elements of the array can be zero 0 as well.
Input Format
First line denotes the number of testcases.

First line of each testcase denotes the size of the array nums.
The next line contains the n elements as space seperated integers.
Output Format
One line for each testcase, denoting the result array as space-seperated integers.

Sample Input
1
4
1 2 3 4
Sample Output
24 12 8 6
'''
test=int(input())

for i in range(test):
	n=int(input())
	lst=list(map(int,input().split()))

	if n==1:
		print(1)
	left=[0]*n
	right=[0]*n
	prod=[0]*n
	left[0]=1
	right[n-1]=1
	for i in range(1,n):
		left[i]=lst[i-1]*left[i-1]
	for j in range(n-2,-1,-1):
		right[j]=lst[j+1]*right[j+1]
	for i in range(n):
		prod[i]=left[i]*right[i]
	for i in range(n):
			print(prod[i],end=" ")