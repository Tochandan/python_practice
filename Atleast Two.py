'''
Atleast Two
You have an array of size n. You need to find all such elements of the given array, who have atleast 2 unique elements greater than it in the same array. Print all such unique elements as space seperated values (in non-decreasing order). If there are no such values, print -1.

Input
One integer, denoting n the size of the given array. Next line containing n space seperated values, denoting the elements of the array.

Output
Print all the values that satisfy the given conditions as space space seperated values (in non-decreasing order). If there are no such values, print -1.

Example
Input1:

6
3 2 2 5 4 5
Output1:

2 3
'''
# your code goes here
n=int(input())
lst=[int(x) for x in input().split()]
lst1=set(lst)
res=list(lst1)
if len(res)<3:
	print(-1)
else:
	for i in range(len(res)-2):
		print(res[i],end=" ")