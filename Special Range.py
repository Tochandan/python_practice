'''
Special Range
Given a range, as [m, n] both inclusive, print all non-negative integers in the range.

Input
First line contains an integer which is starting value of range, say m

Second line contains an integer which is ending value of range, say n

Output
Print all non-negative integers in that range. One integer per line.

If no such integers exist, print -1.

Example
Input:

-5

4

Output:

0

1

2

3

4
'''
# your code goes here
n1=int(input())
n2=int(input())
if n1<0 and n2<0:
	print(-1)
else:
	for i in range(n1,n2+1):
		if i>=0:
			print(i)