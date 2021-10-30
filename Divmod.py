'''
Divmod
Programming language isn't just its technical implementation — it's also a human community. The four widespread multilingual programming languages have had better luck so far with fostering that community than the solitary non-English-based programming languages, but it's still a critical bottleneck.

You need to find useful resources when you Google your error messages. Heck, you need to figure out how to get the language up and running on your computer at all. That's why it was so important that the first web browser let you edit — not just view — websites, why Glitch has made such a point of letting you edit working code from inside a browser window and making it easy to ask for help.

Consider divmod inbuilt function python as the member of python family, just like we do consider oven while roasting. That means rosting can also be done without oven, but using oven makes our job easier.

A brief info about divmod function:

inbuilt python function
takes two arguments (a,b)
returns a tuple containing the quotient of a/b first and then the remainder a.
>>> print divmod(177,10)
(17, 7)
Given two integer inputs, print the outputs as mentioned in the output format.

Input Format
The first line contains the first integer, a , and the second line contains the second integer, b.

Output Format
The first line should be the first integer of divmod tuple. The second line should be the second integer of divmod tuple. The third line prints the divmod of a and b (complete tuple).

Sample Input
177
10
Sample Output
17
7
(17, 7)
'''
# # your code goes here
def Divmod(a,b):
	lst=[]
	lst.append(a//b)
	lst.append(a%b)
	x = tuple(lst)
	return x
a=int(input())
b=int(input())
y=Divmod(a,b)

print(y[0])
print(y[1])
print(y)