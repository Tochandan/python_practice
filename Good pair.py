'''
Good Pairs
Given an array of integers nums (length of nums > 1).

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

Input
Single line containing a list of numbers separated by spaces

Output
Single integer representing total number of good pairs

Example
Input:

1 2 3 1 1 3

Output:

4

Explanation:
(0,3), (0,4), (3,4), (2,5) index position elements
'''
# your code goes here

#count (1) - 3- no. of good pairs - 3C2 = 3 
#count (2) -1 =0

#count(3) 2 =2C2=1

arr=[int(x) for x in input().split()]
arr.sort()
goodpairs=0
count=1
for i in range(1, len(arr)):
    if arr[i]==arr[i-1]:
        count += 1
    else:
        goodpairs +=((count* (count-1))//2) #nc2 
        count=1
goodpairs += ((count*(count-1))//2) 
print(goodpairs) # nC2