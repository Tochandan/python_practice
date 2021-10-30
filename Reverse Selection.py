'''
Reverse Selection
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

The subarray which is already sorted.
Remaining subarray which is unsorted.
In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.

This is the logic for normal selection sort. You need to modify and implement this logic in such a way, so that if can sort the array in reverse way. Complete reverseSelectionSort function.

Input
First line contains one integer t, denoting number of testcases. Its is followed t lines:

First line of each testcase contains one integer denoting n.
Second line of each testcase contains n space seperated integers, denoting the elements of the array.
Output
One line for each testcase, denoting the space seperated values of reverse-sorted array.

Example
Input:

2
5
5 10 2 4 -2
4
2 89 90 7
Output:

10 5 4 2 -1
90 89 7 2
'''
def reverseSelectionSort(A, n):
	A.sort(reverse=True)
	return A

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(*reverseSelectionSort(arr, n))