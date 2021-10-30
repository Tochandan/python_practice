'''
Alternate 101
You have been given an array of size N. You need to find the sum of alternate values in the given array, starting from the first element.

Input
One integer, denoting N, the size of the array. The next line contains N space seperated integers, denoting the elements of the given array.

Output
One Integer, denoting the required sum.

Example
Input1:

7
1 4 6 8 9 0 -34
Output1:

-18
Explanation:

1 + 6 + 9 - 34 = -18

'''
n=int(input())
lst=list(map(int,input().strip().split()))[:n]
total=0
for i in range(n):
	if i%2==0:
		total=total+lst[i]
print(total)