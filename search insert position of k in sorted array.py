'''
search insert position of k in sorted array
Given a sorted array arr[] consisting of N distinct integers and an integer K, the task is to find the index of K, if it’s present in the array arr[] then print its index. Otherwise, find the index where K must be inserted to keep the array sorted.

Note:Consider 0 based indexing

Input
First line is an integer T, representing total number of test cases. For each testcase, 1st line containing space separated integers of array from left to right. For each testcase, 2nd line contains number of element to be inserted in given array. For each testcase, 3rd line contains space separated integers of array from left to right to be inserted.

Output
For each new line containing the result for each test input of a test case.

Example
Input: 2

1 5 6 8 9

2

7 4

7 9 17 90

3

0 9 99

Output: 3

1

0

1

4
'''
# your code goes here
def index(arr,k):
	n=len(arr)
	start=0
	end=n-1
	while start<=end:
		mid=(start+end)//2
		if arr[mid]==k:
			return mid
		elif arr[mid]<k:
			start=mid+1
		else:
			end=mid-1
	return end+1
for i in range(int(input())):
	arr=[int(x) for x in input().split()]
	queries=int(input())
	q=[int(x) for x in input().split()]
	for i in range(queries):
		k=q[i]
		print(index(arr,k))