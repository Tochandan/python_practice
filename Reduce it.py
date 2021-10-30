'''
Reduce it
You have been given an integer n. You need to do the following operations unless these operations are no longer applicable to it, and that final value will denote the result.

The operations are:

Subtract 21, if it is odd and positive.
Subtract 11, if it is even and positive.
Input Format:
One integer denoting n.

Output Format:
One integer denoting the resultant integer.

Example:
Input:

35
Output:

-18
Explanation:

The following transformations will take place: 35 -> 14 -> 3 -> -18

'''
# your code goes here
n=int(input())
while n>0:
	if n%2==0:
		n=n-11
	else:
		n=n-21
print(n)