'''
Add Strings
Description
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.

Both num1 and num2 contains only digits 0-9.

Both num1 and num2 does not contain any leading zero.

You MUST NOT convert the inputs to integer directly.

Complete the addStrings function. It takes the input as two strings & you need to return the string (which will same as the addition of two number as integers).
'''
 # Complete this addStrings() function

def addStrings(num1, num2):
	num1=num1[::-1]
	num2=num2[::-1]
	res=""
	if len(num1)<len(num2):
		num1,num2=num2,num1
	carry = 0
	for i in range(len(num2)):
		temp=int(num1[i])+int(num2[i])+carry
		res+=str(temp%10)
		carry=temp//10
	for i in range(len(num2),len(num1)):
		temp=int(num1[i])+carry
		res+=str(temp%10)
		carry=temp//10
	if carry!=0:
		res+=str(carry)
	return res[::-1]
		
 

## Do not change anything below this line:

for _ in range(int(input())):
    n1, n2 = input().split()
    print(addStrings(n1,n2)) 