'''
Two Friends
You and your friend Ravi are playing a video game. You have some n fire-balls and Ravi has m fire-balls. The power of each these fire-balls is known.

In the game, each of you will get one chance to attack the other one. You will get this chance as round1 and Ravi will get the chance as round2

The rule of the game is, while a person A attacks the other one B, the result of that round is the distinct powers of fire-balls which exist in A but not in B.

Output the combined result of both the rounds in sorted order.

Input Format
The first line contains the integer, n. The next line denotes the powers of those n fire-balls (belonged to you). The next line contains the integer, m. The next line denotes the powers of those m fire-balls (belonged to Ravi).

Output Format
Output the result as one integer in each line.

Sample Input
4
2 4 5 9
4
2 4 11 12
Sample Output
5
9
11
12

'''
# your code goes here
n=int(input())
arr1=set([int(x) for x in input().split()])
m=int(input())
arr2=set([int(x) for x in input().split()])
res1=arr1.difference(arr2)
res2=arr2.difference(aar1)
res=list(res1)+list(res2)
res.sort()
for i in res:
	print(i)
