'''
Amazing Sum
You have been given n integer values. Lets say the given values are a1, a2, a3, a4 ...

If the sum of two consecutive input values is greater than 100, then the given values have amazing sum

Input Format:
First line denotes n, the number of inputs. The next n lines contains one integer in each line.

Output Format:
One string, either True or False, denoting whether the given values has amazing sum or not.

Example:
Input:

5
10
20
30
40
50
Output:

False
Explanation:

The maximum sum of two consecutive values here is 90, which is not greater than 100, so the answer is False.
'''
# your code goes here
n=int(input())
lst=[]
flag=1
for i in range(n):
	lst.append(int(input()))
for i in range(1,n):
	if lst[i]+lst[i-1]>100:
		print(True)
		flag=0
		break
if flag==1:
	print(False)