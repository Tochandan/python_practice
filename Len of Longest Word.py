'''
Len of Longest Word
Given a string S, find the length of the longest word in the string. The words are separated by Spaces. If no such word exists, print 0

Input
one line containing the String S

Output
one line containing the length of the longest word in the String S

Example
Input: hello world

Output: 5 - because both words are of length 5

Input: helloooooo world

Output: 10 - because "helloooooo" is of length 10
'''
######################
n=list(map(str,input().split()))
lst=[]
for i in range(len(n)):
    lst.append(len(n[i]))
print(max(lst))
    
