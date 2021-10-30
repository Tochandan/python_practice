'''
Single Number
Given a list of N integers, every element appears twice except for one. Find that single one.

Input
First number is N (the number of integers given) Followed by the N numbers

Output
One line containing the output integer

Example
Input: 3

2

2

1

Output: 1

Input: 5

2

2

1

1

3

Output: 3
'''
#########################
# your code goes here
n=int(input())
lst=[]
for i in range(n):
	lst.append(int(input()))
sum_uniq=sum(set(lst))
sum_lst=sum(lst)
print(sum_uniq*2-sum_lst)