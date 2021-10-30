'''
longest-substring
Description
Given a string s, find the length of the longest substring without repeating characters.

Constraints:

0 <= s.length <= 10^4
s consists of English letters, digits, symbols and spaces.
Input format
First line denotes t, denoting the number of tescases. Each test case contains a string s in one line.

Output format
One line for each test case.

Sample input
3
abcabcbb
bbbbb
Sample output
3
1
0
Explanation
For the first testcase, the answer is "abc", with the length of 3.
For the second testcase, the answer is "b", with the length of 1.
For the third testcase, the answer is "", with the length of 0.
'''
# your code goes here
def longeststr(s):
	#abcdefcz->6
	if s=="":
		return 0
	last_occurance=[-1]*256
	left=-1
	res=0
	for i in range(len(s)):
		left=max(left,last_occurance[ord(s[i])])
		len_substr=i-left
		res=max(res,len_substr)
		last_occurance[ord(s[i])]=i
	return res

for i in range(int(input())):
	s=input()
	print(longeststr(s))