'''
High Avg
Description
You are given an array A of length N. You have to choose a subset S from given array A, such that average of S is less than K. You need to print the maximum possible length of S.

Just need to implement where_to_place_X function.

Expected Complexity NlogN.

Input
The first line of each input contains N, length of array A.

Next line contains N space separated elements of array A.

Next line of input contains an integer Q, Number of queries.

Each following Q lines contains a single integer K.

Output
For each query, print single integer denoting the maximum possible length of the subset.

Example
Input: 5

1 2 3 4 5

5

1

2

3

4

5

Output:

0

2

4

5

5

Explanation
In first query, there is no possible subset such that its average is less than 1.

In second query, you can select the subset {1,2}.

In third query, you can select the subset {1,2,3,4}.

In fourth and fifth query, you can seelct the complete array {1,2,3,4,5}.
'''
def Where_to_place(a, k):
   # Implement This
    start = 0
    end = len(a)-1

    while start<=end:
    	mid = (start+end)//2
    	if a[mid]<k:
    		start = mid+1
    	else:
    		end = mid-1
    return start
    	
n=int(input())
l=list(map(int,input().split()))[:n]
sum=0
l.sort()
for i in range(n):
    sum+=l[i]
    avg=sum//(i+1)
    l[i]=avg   
t=int(input())    
for k in range(t):
    x=int(input())
    print(Where_to_place(l,x))