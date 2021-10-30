'''
Full Power
Given an array A having N distinct integers.

The power of the array is defined as:

max(A[i]-A[j]) where 2 <= i <= N
for each i, j is the largest index less than i such that A[j] < A[i].
Let's say the array is {1,2,5}, then the power of the array is max((2-1), (5-2)), which simplifies to max(1,3) which is equal to 3.

Operation Allowed: If you are allowed to choose any two indices x and y and swap A[x] and A[y], find out the maximum power that can be achieved.

Note:
You are allowed to perform the above operation at most once.

Input
First line consists of a single integer, T, denoting the number of test cases. First line of each test case consists of a single integer, denoting N. Second line of each test case consists of N space separated integers denoting the array A.

Output
For each test case, print the maximum achievable power on a new line.

Constraints:
1 ≤ T ≤ 10
1 ≤ N ≤ 10^5
1 ≤ A[i] ≤ 10^9
Example
Input:

2

2

9 10

4

2 3 4 1

Output:

1

3

Explanation
In the first test case, we don't need to do any swaps, the max achievable power is 1. In second test case we can swap A[3] and A[4] so the array will be 2 3 1 4 and the power will be 3
'''
# your code goes here
for i in range(int(input())):
	n=int(input())
	a=[int(x) for x in input().split()]
	b=[]
	for i in range(n):
		b.append(a[i])
	b.sort()
	if(n==2):
		print(abs(a[0]-a[1]))
		continue
	if(a[0]==b[n-1] and a[n-1]==b[0] and n!=2):
		print(max(b[n-2]-b[0],b[n-1]-b[1]))
	else:
		print(b[n-1]-b[0])
	