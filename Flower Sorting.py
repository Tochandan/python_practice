'''
Flower Sorting
You have an array of size n, which contains type of flowers we have. There can be total 5 types of flowers only (1, 2, 3, 4, 5). You need to sort those flower types in the array.

Expected Time Complexity : O(n) Expected Auxiliary Space : O(1)

Input
One integer, denoting n the size of the given array. Next line containing n space seperated values, denoting the elements of the array.

Output
Sorted array of flower types, as space seperated values.

Example
Input1:

5
3 2 5 4 5
Output1:

2 3 4 5 5
'''
# your code goes here
from collections import Counter
n=int(input())
arr=[int(x) for x in input().split()]
count=Counter(arr)
for i in range(n):
	if i<count[1]:
		arr[i]=1
	elif i<(count[1]+count[2]):
		arr[i]=2
	elif i<(count[1]+count[2]+count[3]):
		arr[i]=3
	elif i<(count[1]+count[2]+count[3]+count[4]):
		arr[i]=4
	else:
		arr[i]=5
print(*arr)