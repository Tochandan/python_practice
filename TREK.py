'''
TREK
You went on a trek with HEC(Himalayan Explorers' Club). The trek was to a very beautiful place known as Valley of Flowers'.

For each step you took on the trek, you noted it down as U for Upward and D as Downward. (

Assume, these are the only two possible types of steps possible on the trek.
Trek/Hike always start and end at sea level, and each step up or down represents a unit change in altitude.
A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

Input Format
First line denotes the number of testcases. For each testcase:

First line denotes the number of steps, N.
The next line contains a string of length N containing only U and D.
Output Format
For each testcase, print the number of valleys walked through in a new line.

Sammple Input
1
8
UDDDUDUU
Sample Output
1
Explanation
If we represent _ as sea level, a step up as /, and a step down as \, the hike can be drawn as:

_/\      _
   \    /
    \/\/

The hiker enters and leaves one valley.
'''
# your code goes here
def countvalley(n,step):
	alt=0
	valley=0
	if step[0]=="U":
		alt+=1
	else:
		alt-=1
	for i in range(1,n):
		if step[i]=="U":
			alt+=1
		else:
			alt-=1
		if alt==0:
			if step[i]=="U":
				valley+=1
	return valley
	
for i in range(int(input())):
	n=int(input())
	step=input()
	print(countvalley(n,step))
	
