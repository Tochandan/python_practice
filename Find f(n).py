'''
Find f(n)
For a positive integer n let's define a function f:

f(n) =  - 1 + 2 - 3 + .. + ( - 1)^n*n

Your task is to calculate f(n) for a given integer n.

Input
Only line of input contains the n.

Output
Print the corresponding value of f(n).

Example
Input:

100

Output:

50
'''
# your code goes here
n=int(input())
if n%2==0:
	print(n//2)
else:
	print(-(n+1)//2)
