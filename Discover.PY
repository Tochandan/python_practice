'''
Discover
Description
You are given an array A of size N, and Q queries to deal with. For each query, you are given an integer X, and you're supposed to find out if X is present in the array A or not.

You need to implement a find function in there.

The code should run in NlogN complexity.

Input
The first line contains two integers, N and Q, denoting the size of array A and number of queries. The second line contains N space separated integers, denoting the array of elements Ai. The next Q lines contain a single integer X per line.

Output
For each query, print YES if the X is in the array, otherwise print NO.

Example
Input: 5 10

50 40 30 20 10

10

20

30

40

50

60

70

80

90

100

Output:

YES

YES

YES

YES

YES

NO

NO

NO

NO

NO

Explanation
'''
def find_k(a, k):
    # Implement this and return YES if found else return No
    
    start = 0
    end = len(a) -1
    

    
    while start <= end:
    	mid = (start + end)//2
    	if a[mid] == k:
    		return 'YES'
    	
    	elif k < a[mid]:
    		end = mid - 1

    	elif k > a[mid]:
    		start = mid + 1

    return 'NO'
    
    
from sys import stdin
N,Q = input().split()
a = list(map(int,input().split(' ')))
a.sort() 
for i in range(int(Q)):
    k = int(input())
    print(find_k(a, k))