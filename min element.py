'''
min element
Description
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]). You have to return the minimum element of the array .

Expected Time Complexity: O(log n)

Input format
First line contains a positive integer n, denoting the number of elements in array. Next line contains n space separated integers sorted in ascending order and rotated at some pivot as explained above.

Output format
Single line containing the minimum element in the array.

Sample input
5
3 4 5 1 2
Sample output
1
Explanation
1 is the minimum element in the given array. Initially sorted array must be [1,2,3,4,5] which on rotation becomes [3,4,5,1,2]
'''
# your code goes here
def minele(arr,n):
	if n==1:
		return arr[0]
	start=0
	end=n-1
	while start<=end:
		mid=(start+end)//2
		if mid-1>=0 and mid+1<n:
			if arr[mid-1]>=arr[mid] and arr[mid]<=arr[mid+1]:
				return arr[mid]
		elif mid-1>=0:
			if arr[mid-1]>=arr[mid]:
				return arr[mid]
		elif mid+1<n:
			if arr[mid]<=arr[mid+1]:
				return arr[mid]
		if arr[mid]<arr[end]:
			end=mid-1
		elif arr[mid]>arr[end]:
			start=mid+1
n=int(input())
arr=[int(x) for x in input().split()]
print(minele(arr,n))
				
			