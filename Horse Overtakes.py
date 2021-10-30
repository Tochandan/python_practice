 '''
 Horse Overtakes
Your task is to calculate the number of overtakes in a horse race. You are given data of the horses' velocities and their starting positions. The race length is extremely long, 10^(10000)

About the horses:

There are n horses
Each has in index from 0 to n-1
About the data:

Each horse has a velocity v, 0 <= v <= 10
eACh horse has a starting position in the race p, 0 <= p <= n-1
Each horse starting position is unique, i.e. no two horses have the same starting position
For convenience, we'll denote the starting position of horse with idx A as p[A] About starting positions:

A horse with a lower starting position implies it is farther away from the finish line
For horses A and B, if p[A] > p[B] then A is closer to the finish line
About overtakes:

An overtake is when a horse B finishes the race before A, and p[A] > p[B]
Input
The first line contains n, the number of horses This is followed by n lines, each containing 2 integers, position p and velocity v

Output
One line containing an integer indicating the number of overtakes that happened during the race

Example
Input:

6

1 7

3 10

0 5

4 3

5 7

2 4

Output:

7

Explanation
The first line is 6 indicating a total of 6 horses

The next lines contain the position and velocity of each horse

The output is the number of overtakes happening through the race, 7 and this is the value in the output
 '''
test=int(input())
p=[0]*test
for i in range(test):
	a,b=map(int,input().split())
	p[a]=b
d=[0]*11
overtake=0
for i in range(test):
	vel=p[i]
	for j in range(vel+1,11):
		overtake += d[j]
	d[vel] += 1
print(overtake)
