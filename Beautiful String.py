'''
Beautiful String
A string is beautiful if it has equal number of a,b,and c in it.

Example "abc" , "aabbcc" , "dabc" , "" are beautiful.

Given a string of alphabets containing only lowercas aplhabets (a-z), output the number of non-empty beautiful substring of the given string.

Input
The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows. Each test case consists of a line containing a string a length L.

Last contain value of K.

Output
For each test case, output a single line containing the number of beautiful substring.

Example
Input:

2

abacbcba

dbacd

Output:

5

6

Explanation
Test Case 1 The output will be 5 ("abacbc","bac",”acb”, ”acbcba”,"cba")

Test Case 2 The output will be 6 ("d", "dbac", "dbacd", ”bac”, "bacd", "d")
'''
# your code goes here
from collections import defaultdict

#obacbcba> 0 [1, -1, 0, 12, 3, 8, 121, 12, 2, 1, 0, 1, 1]

def beautiful(st):
	counta, countb, countc= 0,0,0 
	d=defaultdict(int)
	d[(0,0)] = 1
	res=0
	for i in st:
		if i=='a':
			counta+= 1
		elif i=='b':
			countb += 1
		elif i=='c':
			countc += 1
		z =(counta-countb, counta-countc)
		res+= d[z]
		d[z]+=1
	return res

for i in range(int(input())):
    st=input()
    print(beautiful(st))

# adding the previous number of occurence # updating the number of occurence I