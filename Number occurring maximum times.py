'''
Number occurring maximum times
Given a list of N integers sorted in ascending order, Please find the number which occurs 4 times in the array

Input
First number is N (the number of integers given) Followed by the N numbers

Output
Print the number which occurs 4 times. print -1 if such a number doesnt exist

Example
Input: 10

1

2

3

4

4

4

4

5

6

6

Output: 4
'''
####################
n=int(input())
lst=[]
flag=0
for i in range(n):
    lst.append(int(input()))
for i in range(n):
    no=lst.count(i)
    if no==4:
        flag=1
        print(lst[i])
        break
if flag==0:
    print(-1)