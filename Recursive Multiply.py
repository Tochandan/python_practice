'''
Recursive Multiply
You have been given an integer n. You need to print all the multiplication of all the digits of the n using recursion.

Note: DO NOT USE LOOP/s
Input
First line contains one integer t, denoting number of testcases. Its is followed t lines:

Each line contains one integer denoting n.
Output
One line for each testcase, denoting the result.

Example
Input:

2
12345
356045873
Output:

120
0
'''
# your code goes here
def recursiveMultiply(n):
	if n<=9:
		return n
	return ((n%10)*recursiveMultiply(n//10))
for i in range(int(input())):
	n=int(input())
	print(recursiveMultiply(abs((n))))