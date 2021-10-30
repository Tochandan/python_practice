'''
Bat-Man
Batman has defeated Hugo Strange and now he is getting bored as there is too much peace in Gotham City. Now, to pass his time he wants to perform a operation on an array. A left rotation operation on an array shifts each of the array's elements 1 unit to the left. For example, if 2 left rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2]. Note that the lowest index item moves to the highest index in a rotation. This is called a circular array.

Given an array a of integers and a number, d , perform d left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.

Input Format
The first line denotes the number of testcases. For each testcase:

The first line contains two space-separated integers n and d , i.e., the size of a and the number of left rotations.
The second line contains n space-separated integers, each an a[i].
Output Format
Space seperated integers denoting the respective elements of the resultant array.

Sample Input
1
5 4
1 2 3 4 5
Sample Output
5 1 2 3 4
Explanation
When we perform d = 4 left rotations, the array undergoes the following sequence of changes:

[1,2,3,4,5] -> [2,3,4,5,1] -> [3,4,5,1,2] -> [4,5,1,2,3] -> [5,1,2,3,4]
'''
# your code goes here
def rotate(arr,n,res):
	result=[0]*n
	for i in range(n):
		result[(i+res)%n]=arr[i]
	return result
	
for i in range(int(input())):
	n,l=map(int,input().split())
	arr=[int(x) for x in input().split()]
	res=0
	res-= l
	print(*rotate(arr,n,res))