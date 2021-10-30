'''
Fun Five
Description
You are given an integer N.

Write a program to find a minimum number P such that SUMMATION(F(X))>=N for range of X as 1<=X<=P, ( where F(X) represents the number of times X can be divided by 5 ).

For 1<=X<=P, SUMMATION(F(X)) is defined as F(1)+F(2)+F(3)+...+F(P)

So, overall: Find Minimum vale of P such that, F(1)+F(2)+F(3)+...+F(P) <= N.

Example:

F(250) = 3

250/5 = 50, 50/5 = 10, 10/5 = 2: As 2 cannot be divided by 5, the procedure stops here.
Input format
First line: T (Number of test cases)
First line in each test case: N
Output format
For each testcase, print the minimum number P in seperate line.

Sample input
2
1
2
Sample output
5
10
Explanation:
Second case, n=2, now start checking from 1, since 1,2,3,4,6,7,8,9 are not divisible by 5, so for count 2 minimum P will be 10.
'''
# your code goes here
def get(num):
	ret=0
	while num!=0:
		ret+=num//5
		num=num//5
	return ret
for i in range(int(input())):
	n=int(input())
	low=0
	high=10**18
	ans=high
	while low<=high:
		mid=(low+high)//2
		val=get(mid)
		if val>=n:
			high=mid-1
			ans=min(ans,mid)
		else:
			low=mid+1
	print(ans)
	