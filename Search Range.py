'''
Search Range
Given a sorted array of integers A of size N. Find the start and the ending index of the numbers in the given range (inclusive of start and ending point).

Your algorithm’s runtime complexity must be in the order of O(log n).

Return -1 -1 if there are no elements in the given range.

Input format
First line contains a positive integer N, denoting the number of elements in the array. The next line of the input contains N space seperated integers, which are the elements of the given array. The next line contains 2 integers, which specifies the range, we need to search.

Output format
2 space seperated integers, denoting the result.

Sample input1
6
1 2 3 3 4 5
3 4
Sample output1
2 4
Explanation1
The starting index of 3 is 2 and the ending index of 4 is 4.

Sample input2
10
1 2 3 3 4 4 7 7 10 10
5 6
Sample output2
-1 -1
Explanation2
There are no elements in the range of 5 to 6. Hence, the output is -1,-1.
	

'''
# your code goes here
# your code goes here
def first_occ(arr,n,left):
	start,end=0,n-1
	result=-1
	while start<=end:
		mid=(start+end)//2
		if arr[mid]>=left:
			result=mid
			end=mid-1
		else:
			start=mid+1
	return result
def last_occ(arr,n,x):
	start,end=0,n-1
	result=-1
	while start<=end:
		mid=(start+end)//2
		if arr[mid]<=right:
			result=mid
			start=mid+1
		else:
			end=mid-1
	return result
n=int(input())
arr=[int(x) for x in input().split()]
left,right=map(int,input().split())
a,b=first_occ(arr,n,left),last_occ(arr,n,right)
if a<=b:
	print(a,b)
else:
	print(-1,-1)