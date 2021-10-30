'''
Noor Pond
Noor is going fish farming. There are N types of fish. Each type of fish has size(S) and eating factor(E). A fish with eating factor of E, will eat all the fish of size <= E.

Help Noor to select a set of fish such that the size of the set is maximized as well as they do not eat each other.

Input
The first line contains T, the number of test cases. The first line of a test case contains an integers N. N is the number of types of fish. Each of the next N lines contains two integers S and E meaning the size and eating factor of a fish.

Output
For each test cases, print a single integer, the maximum number of fish Noor can have in his pond.

Example
Input:

1

3

4 1

5 4

7 3

Output:

2

Explanation
In the sample input, Noor can select the first and the third fish
'''
# your code goes here
for i in range(int(input())):
	n=int(input())
	size=[]
	eating=[]
	for i in range(n):
		s,e=map(int,input().split())
		size.append(s)
		eating.append(e)
	size.sort()
	eating.sort()
	count=n
	j=0
	for i in range(n):
		if eating[i] >= size[j]:
			count-=1
			j+=1
	print(count)
		
	