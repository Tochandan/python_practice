'''
Vowels 101
You have been given a string s as input. You need to find the number of vowels present in this given string.

Input
One line containing the string s. (The string will only contain lowercase letters)

Output
One Integer, denoting the result.

Example
Input1:

academy
Output1:

3

'''
# your code goes here
s=input()
count=0
for i in s:
	if i=="a" or i== "e" or i== "i" or i== "o" or i== "u" :
		count+=1
print(count)
	