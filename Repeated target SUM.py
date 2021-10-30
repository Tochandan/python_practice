'''
Repeated target SUM
You have been given an array of distinct integers and a "key". find out the total number of ways in which we can obtain the "key" by summing up one or more elements of the array such that one element from the array can be used multiple times.

[ordering of elements does not matter. i.e- {1,2,2,3} is same is {3,1,2,2} and thus they are considered as one]

Constraints
1<= N <= 10

0 < arr[i], elements are distinct

0 < key

Input
First line of the input contains N,key(space separated). second line of the input contains the N elements of the array.

Output
Print the total number of ways in which we can obtain "key" by summing up one or more elements of the array(repetition allowed)

Example
Input:

3 4

1 2 3

Output:

4

Explanation:

possible solutions- (1,1,1,1),(1,1,2),(1,3),(2,2)
'''
def repeatsum(arr,n,k,i):
	if k==0:
		return 1 
	if k<0 or i==n:
		return 0
	return repeatsum(arr,n,k-arr[i],i)+repeatsum(arr,n,k,i+1)
n,k=map(int,input().split())
arr=list(map(int,input().split()))
print(repeatsum(arr,n,k,0))
