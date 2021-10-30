'''
Triangle Perimeter
Description
Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.

Input format
First line is an integer T, representing total number of test cases.

T lines containing space separated integers. Count of these integers >= 3

Output format
T lines, each line containing the perimeter for each test case.

Sample input
3

9 4 2 5 6 8

65 150 29 38

1 3 5

Sample output
23

132

0

Explanation
For the first test case, we can pick 9, 6, 8 whose perimeter is 23

For the second test case, we can pick 65, 29, 38 whose perimeter is 132

For the third test case, no triangle can be formed. So, 0
'''
# your code goes here
def maxPerimeter(arr):
    maxi = 0
    n = len(arr)
    arr.sort(reverse = True)
 
    for i in range(0, n - 2):
        if arr[i] < (arr[i + 1] + arr[i + 2]):
            maxi = max(maxi, arr[i] +
                       arr[i + 1] + arr[i + 2])
            break
 
    if(maxi == 0):
        return 0
    else:
        return maxi
n=int(input())
for i in range(n):
	arr=list(map(int,input().split()))
	print(maxPerimeter(arr))