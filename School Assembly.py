'''
School Assembly
Description
In Dehradun Public School (DPS), they are having an assembly on the monday morning. All the Students of class 10th are standing in a single queue. There are several student groups in the queue. The pricipal Ms. Sharmila wants to find out the minimum number of student groups that are atleast present in the queue.

Since, she doesn't want any ambiquity in the answer, she asks you to write the code for finding this out. The speciality of each group is that: Each group has group members standing in non-decreasing order of their height.

Input
The first line of input contains one positive integer N, denoting the number of students. The second line contains N space-separated integers H[i] denoting the height of i-th student.

Output
Print the minimum number of groups that are at least present in the queue.

Example
Input:

4
1 2 3 4
Output:

1
'''
# your code goes here
n=int(input())
arr=[int(x) for x in input().split()]
ans=1
for i in range(1,n):
	if arr[i]<arr[i-1]:
		ans+=1
print(ans)