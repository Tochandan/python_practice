'''
First & Last
Description
Given a sorted array with possibly duplicate elements, the task is to find indexes of first and last occurrences of an element x in the given array.

Note:
If the number x is not found in the array just print -1 -1. Your algorithm’s runtime complexity must be in the order of O(log n).

Input format
First line contains a positive integer N, denoting the number of elements in the array. The next line contains n space seperated integers. The next line contains a target integer x.

Output format
Two space seperated integers denoting the first and last occurrences of x

Sample input
6
5 7 7 8 8 10 
8
Sample output
3 4
Explanation
The starting index of 8 is 3 and the ending index of 8 is 4.

Sample input
6
5 7 7 8 8 10 
6
Sample output
-1 -1
Explanation
There is no occurence of 6. Hence, the starting and ending index are marked as -1 and -1.
'''
# your code goes here
def first(arr,n,x):
	start,end=0,n-1
	result=-1
	while start<=end:
		mid=(start+end)//2
		if arr[mid]==x:
			result=mid
			end=mid-1
		elif arr[mid]>x:
			end=mid-1
		else:
			start=mid+1
	return result
def last(arr,n,x):
	start,end=0,n-1
	result=-1
	while start<=end:
		mid=(start+end)//2
		if arr[mid]==x:
			result=mid
			start=mid+1
		elif arr[mid]>x:
			end=mid-1
		else:
			start=mid+1
	return result
n=int(input())
arr=[int(x) for x in input().split()]
x=int(input())
print(first(arr,n,x),last(arr,n,x))