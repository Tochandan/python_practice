'''
Sort 2's
You have been given an array of integers 'A' of size 'N'. Rearrange the array on the basis of the number of times '2' occurs in the number. The number with greater number of 2's comes first in the rearranged list. If two numbers have same number of 2's present, the greater of the two numbers comes first.

Constraints
0 <= A[i] <= 10000000000 , 0 <= N <=100000

Input
First line of the input contains N(size of the input array), the second line contains the 'N', space separated integers representing the elements of the array.

Output
Print the elements of the array(space separated) after rearranging them on the logic provided above.

Example
Input:

5

25 988888 22 52222 2992

Output:

52222 2992 22 25 988888

Explanation:

52222-> 4 2's

2992-> 2 2's

22->2 2's

25-> 1 2's

988888->0 2's

2992 and 22 have same number of 2's but 2992 is bigger of the two hence it comes first.
'''
# your code goes here
n=int(input())
arr=[int(x) for x in input().split()]
arr.sort(reverse=True)
arr.sort(key=lambda x:(str(x).count("2")),reverse=True)
print(*arr)