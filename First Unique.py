'''
First Unique
Description
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Note: A non repeating character is the one that occcurs only one time.

Input
First line of each input contains an integer T denoting the number of test cases.

First line of each test case contains a string .

Output
For each test case print the index of first non-repeating character or else return -1 if no non-repeating character exists.

Example
Input:

2

abc

aa

Output:

0

-1

Explanation
In first test case, 'a' is the first non repeating character and its index is 0.

In second test case, 'a' occurs 2 times thus only repeating character exists hence answer is -1.
'''
# your code goes here
for _ in range(int(input())):
	string=input()
	dict={}
	ans=-1
	for i in range(len(string)):
		if(string[i] not in dict ):
			dict[string[i]]=i
		else:
			dict[string[i]]=-1
	for key in dict:
		if dict[key]!=-1:
			ans=dict[key]
			break
	print(ans)