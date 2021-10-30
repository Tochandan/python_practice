'''
Case Sort
Given a string S consisting of uppercase and lowercase characters. The task is to sort uppercase and lowercase letters separately such that if the ith place in the original string had an Uppercase character then it should not have a lowercase character after being sorted and vice versa.

Expected Time Complexity: O(N*Log(N)). Expected Auxiliary Space: O(N).

Constraints:
1 ≤ N ≤ 10^3

Input
The first line of input contains integer N the size if the string. Next line denotes the given string.

Output
Print the resultant string

Example
Input1:

12

defRTSersUXI

Output1:

deeIRSfrsTUX

Explanation1:
Sorted form of given string with the same case of character as that in original string is deeIRSfrsTUX

Input2:

6

srbDKi

Output2:

birDKs

Explanation2:
Sorted form of given string with the same case of character will result in output as birDKs.
'''
n=int(input())
s=input()
ulst=[]
llst=[]
res=""

s1=list(s)
for i in s:
	if i.isupper():
		ulst.append(i)
	if i.islower():
	    llst.append(i)
ulst.sort()
llst.sort()
j=0
k=0
for i in range(n):
    if s[i].isupper():
        res=res+ulst[j]
        j+=1
    if s[i].islower():
        res=res+llst[k]
        k+=1
print(res)
        
