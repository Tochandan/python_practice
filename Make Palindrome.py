'''
Make Palindrome
Given a string S of length l and you have to covert that into palindrome using the same string. You will also given a number N, if N is 0 you have a make the palindrome of length 2xl, if N is 1 then the final length will be 2xl - 1.

A string is said to be a palindrome if the string read from left to right is equal to the string read from right to left.

If the length of the given string is 1, you don't have to do anything, just return the string. As every letter is a palindrome of length 1.

Input-1
asdf

0

Output-1
asdffdsa

Input-2
asdf

1

Output-2
asdfdsa

'''
string=input()
n=int(input())
reverse= "".join(reversed(string))
if string==reverse:
		print(string) 
else:
	if n==0:
	    print(string+reverse)
	elif n>0:
			print(string+reverse[1:])
	    
	elif len(string)==1:
	    print(string)