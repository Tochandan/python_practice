'''
Common Alphabets
Given list of strings. The task is to find the frequency of the elements which are common in all strings given in the list of strings.

Input:
First line contains N, number of strings.

Next N lines contians a string in each line.

Output:
N linese each line contains an alphabet and it's frequency in sorted order for each of the input string.

alphabet and the frequency are separated by a space

Problem Constraints:
1<=A.length<=500

1<=A[0].length<=100

Examples:
Input :

3

gefgek

gfgk

kinfgg

Output :

f 1

g 2

k 1

Explanation :
f occurs once in all Strings.

g occurs twice in all the strings.

k occurs once in all string.

Output is in ascending order
'''
# your code goes here
from collections import defaultdict,Counter
n=int(input())
strarr=[]
for i in range(n):
	strarr.append(input())
d=Counter(strarr[0])
for i in range(1,n):
	temp=Counter(strarr[i])
	for i in d:
		if temp[i]==0:
			d[i]=-1
		else:
			d[i]=min(d[i],temp[i])
for key,value in sorted(d.items()):
	if value!=-1:
		print(key,value)