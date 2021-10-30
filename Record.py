'''
Record
Diana plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

For example, assume her scores for the season are represented in the array scores = [12, 24, 10, 24]. Scores are in the same order as the games played. She would tabulate her results as follows:

Game  Score  Minimum  Maximum   Min Max
 1      12     12       12       0   0
 2      24     12       24       0   1
 3      10     10       24       1   1
 4      24     10       24       1   1
This means that she broke the record for Max score in game 2 (this is when the highest score increased), and she broke the record for Min score in game 3 (this is when the lowest score decreased).

Given the scores for a season, find and print the number of times Diana breaks her records for most and least points scored during the season.

Input Format
The first line contains an integer n, the number of games.

The second line contains n space-separated integers describing the respective values of score0, score1, score2, ... ,scoren-1.

Output Format
Print two space-seperated integers describing the respective numbers of times the best (highest) score increased and the worst (lowest) score decreased.

Sample Input
9
10 5 20 20 4 5 2 25 1
Sample Output
2 4
'''
n=int(input())
lst=list(map(int,input().strip().split()))[:n]

countmax=0
countmin=0
maxi=lst[0]
mini=lst[0]
for i in range(1,n):

	if lst[i]>maxi:
	    maxi=lst[i]
	    countmax+=1
	elif lst[i]<mini:
	    mini=lst[i]
	    countmin+=1
res=[countmax,countmin]

print(*res)
