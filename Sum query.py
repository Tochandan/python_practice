'''
Sum query
Given an array of N numbers and q queries are provided each query has a starting index and an ending index find the sum [L, R]. find sum of elements from [L ... R]. Note array indexing starts from 1.

Input
First Line N and Q number of queries (N <= 1e5 and Q <= 1e5).

Then a line of N elements of array

Then of Q lines each line has L and R

Output
Print the sum corresponding to each query

Example
Input:

4 2

1 2 3 4

1 2

3 4

Output:

3

7
'''
n,q=map(int,input().split())
lst=list(map(int,input().strip().split()))[:n]
for i in range(1,q+1):
    add=0
    l,r=map(int,input().split())
    for j in range(l,r+1):
        add=add+lst[j-1]
    print(add)
    
 