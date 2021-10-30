'''
Maximum sum combination
An array of integers contains integers in range {0,1,2,3,4,5,6,7,8,9}. Using these digits as the digits of a number we create two numbers M and N(difference between the total number of digits of M and N should be smaller than or equal to 1}. Find the maximum sum of M,N possible i.e max(M+N).[ You can use an element of the array at most once for generating the two numbers]

Input
First line of the input contains 'N'. the total numbe of integers in the digits array. The next line contains the N space separated integers(each entry is a digit in range 0-9).

Output
Print the maximum sum possible of the two numbers made from the digits of the array.

Example
Input:

6

1 2 3 3 9 7

Output:

1663

Explanation:

for M=932 and N=731, sum is 1663

Input:

7

1 2 9 0 2 3 8

Output:

10141

Explanation:

for M=9320 and N=821 we have sum=10141
'''
n = int(input())                                # for size
lst= list(map(int, input().split(' ')[:n]))
lst.sort(reverse=True)
f = lst[0]
s = lst[1]
for i in range(2,n):
    if(i%2 == 0):
        f = f*10+ lst[i]
    else:
        s = s*10+ lst[i]
print(f+s)