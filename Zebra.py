'''
Zebra
You have been given n non-negative integer values. Lets say the given values are a1, a2, a3, a4 ...

You need to find out whether these values can form a zebra crossing or not (in the same order).

Note that in zebra crossing, there are alternate white colors (denoted as positive numbers here), and empty or black colors (denoted by non-positive numbers here).

Input Format:
First line denotes n, the number of inputs. The next n lines contains one integer in each line.

Output Format:
One value denoting True or False.

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
'''

#################
n=int(input())
lst=[]

for i in range(n):
    lst.append(int(input()))
for i in range(n-1):
    f=0
    if (lst[i]>0 and lst[i+1]<0) or (lst[i]<0 and lst[i+1]>0):
        
        f=1
        
if f==0:
    print(False)
elif f==1:
    print(True)