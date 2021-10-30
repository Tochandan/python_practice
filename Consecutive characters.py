'''
Consecutive characters
Given a string S, find the maximum length of a non-empty substring that contains only one unique character. If such a string doesnt exist, return 0

Input
one line containing the string S

Output
one line containing the maximum length of the substring

Example
Input: beet

Output: 2 Explanation: The substring "ee" is of length 2 with the character 'e' only.

Input: abbcccddddeeeeedcba

Output: 5 Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

Input: triplepillooooow

Output: 5 Explanation: The substring "ooooo" is of length 5 with the character 'o' only.

Input: abc

Output: 1 Explanation: All characters are single characters and not repeated consecutively
'''
# your code goes here
s=input()
res=1
count=1
for i in range(1,len(s)):
	
	if s[i]==s[i-1]:
		count+=1
	else:
		res=max(res,count)
		count=1
res=max(res,count)
print(res)
	
