'''
Rank List
Mid sem marks of a particular subject is announced , since you are curious in knowing your position in class so you decided to make a rank list . You are given the name , scholar number and marks of every student in your class. You have to come up with accurate rank list i.e student having maximum marks at the top and if two students are having same marks then the student having lexicographically smaller name comes first , if both name and marks of the student collide then student having smaller scholar number comes first.

Input
First line of input contains N - Total number of students in class Next N line contains name of student , scholar number and marks scored in exam .

output
Print the ranklist of students as explained above.

Constraints
1 <= N <= 1000

1 <= length of name <= 10

1 <= scholar number <= 1000

0 <= marks <= 30

Sample input
5

b 10 30

a 10 30

a 11 30

b 11 30

c 11 29

Sample output
a 10 30

a 11 30

b 10 30

b 11 30

c 11 29
'''
# your code goes here
# arr =[(1,0),(2,1),(3,3),(3,4),]
#
n=int(input())
arr=[]
for i in range(n):
	name,sch,marks=input().split()
	arr.append([name,int(sch),int(marks)])
arr.sort(key=lambda x:x[1])
arr.sort(key=lambda x:x[0])
arr.sort(key=lambda x:x[2],reverse=True)
[print(*i) for i in arr]
	