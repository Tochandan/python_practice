'''
IS Anagram
You are given two strings A and B, you have to check whether they are anagrams of one another. An anagram is a word that can be obtained by rearranging the characters of the initial word.

Note- DO NOT use the inbuilt sort function at any stage of the code

Input
First line contains the string A and second line contains the string B 1<=len(A),len(B)<=2000

Output
Print "1" if they are anagrams and print "0" if they are not anagrams

Example
Input:

ABABCD

AABBCD

Output:

1

explanation

Since ABABCD can be rearranged to get AABBCD we print "1" as output
'''
# your code goes here
def isAnagram(s1,s2):
	if len(s1)!=len(s2):
		return 0
	count1=[0]*256
	count2=[0]*256
	for i in s1:
		count1[ord(i)]+=1
	for i in s2:
		count2[ord(i)]+=1
	for i in range(256):
		if count1[i]!=count2[i]:
			return 0
	return 1
s1=input()
s2=input()
print(isAnagram(s1,s2))
			