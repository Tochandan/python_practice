'''
Forming names
Description
Given a list of characters of size N and a string x. Return true if characters of the list cqan be used to form string x and if not return false. Note that you can use characters any number of times.

Input format
First line contains a positive integer n that denotes the number of characters in the list. Second line contains a string x that is to be formed using characters of the list. Third line contains n space separated characters of list where each character is a lower case english alphabet.

Output format
For the given list and string print true if string x can be formed using characters of the list any number of times, false otherwise.

Sample input-1
7 
tanmay
y t n m b a r 
Sample output-1
true
Explanation-1
List contains all the alphabets of string 'tanmay'. As characters can be used any number of times we can use 'a' twice to get the string 
Sample input-2
4
ananya
a v n y
Sample output-2
true
Explanation-2
List contains all the alphabets of string 'ananya'. As characters can be used any number of times we can use 'a' thrice, 'n' twice and 'y' once to form the given string. 
Sample input-3
5
anu
a b c u v
Sample output-3
false
Explanation-3
List does not contain 'n', therefore we cannot form string 'anu' by using characters of the list.

'''
# your code goes here
n=int(input())
s=input()
lst=list(map(str,input().strip().split()))[:n]
flag=0
for i in range(len(s)):
	if s[i] in lst:
		flag=1
	else:
		flag=0
		break
if flag==1:
	print("true")
else:
	print("false")