'''
Long Pressed
Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed. Else return False

Input format
The first line contains n, the number of test cases

This is followed by n lines, each containing two strings. The first string is the given name; the second string is the tyed name.

Output format
The output file contains n lines, each either True or False

Sample input
2

alex aaleex

saeed ssaaedd

Sample output
True

False

Explanation
The first line contains 2 indicating 2 test cases.

For the first test case, alex is the actual name, aaleex is the typed name

For the second test case, saeed is the actual name, ssaaedd is the typed name

The outputs are True and False respectively.
'''
def longpressed(a,b):
	if a[0]!=b[0]:
		return False
	i,j=1,1
	while i<len(a) and j<len(b):
		if a[i]==b[j]:
			i+=1
			j+=1
		else:
			if b[j]==b[j-1]:
				j+=1
			else:
				return False
	return i==len(a)

for _ in range(int(input())):
	a,b=input().split()
	print(longpressed(a,b))
	
