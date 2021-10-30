'''
Your Internship
Description
You want to intern at a company, but for that you have to go through a test. There are N candidates applying for the internship including you and only one is to be selected.

The test is as follows:

The candidates are asked to stand in a line at positions 1 to N and given a number K. Now, every Kth candidate remains and the rest are eliminated. This is repeated until the number of candidates are less than K. Out of the remaining candidates, the one standing at smallest position is selected. At what position you must stand to get selected.

Input
First line of input contains a single integer T denoting the number of test cases. The only line of each test case contains 2 space-separated integers N denoting number of candidates and K.

Output
For each test case, print the required position in a new line.

Example
Input:

3
30 3
18 3
5 2
Output:

27
9
4
Explanation:

Case 1 : 
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
3 6 9 12 15 18 21 24 27 30
9 18 27
27

Case 2 : 
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
3 6 9 12 15 18
9 18 (less than K)
9

Case 3 : 
1 2 3 4 5
2 4
4
'''
#1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
#3 6 9 12 15 18 21 24 27 30      3**1
#9 18 27  3**2
#27       3**3
t = int(input())
for _ in range(t):
	n,k = map(int,input().split())
	arr = []
	for i in range(1,n):
		res=k**i
		if res>n:
			print(k**(i-1))
			break
	
