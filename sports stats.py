'''
Sports Stats
Max likes football very much. In order to check the popuplarity of the game, he decided to talk to random people and ask them about their favourite game and note it down in a list.

Given a list of name of people and their favourite sport, help Max in finding the sport liked by most of the people, and also how many people like football.

He could have met same people more than once, he will only count response of his first meet with any person.

Note : Name of person as well as sport is a single string in lowercase. Length of name of people as well as sport is less than 11.

Input
First line will contain no of entries in the list. i.e. N Next N lines will contain two strings, person's name and sports he like.

Output
In first ine, name of sport liked by most no of people (In case of more than one games is liked by highest no of people, output the first one in lexicographical order). In second line, no of people having football as their favourite game.

Example
Input:

7

abir cricket

aayush cricket

newton kabaddi

abhinash badminton

sanjay tennis

abhinash badminton

govind football

Output:

cricket

1

Explanation
2 people likes cricket, ans so it liked by maximum people. 1 person has football as his favourite sport
'''
# your code goes here
from collections import defaultdict

n=int(input())

nameGame={}

gameLike = defaultdict(int)

for i in range(n):
	name, game= input().split()
	if name in nameGame:
	   continue
	else:
		nameGame[name] = game 
		gameLike[game] += 1

max_likes = 0

max_likes_game=""

for i in gameLike:
	if gameLike[i]> max_likes:
		max_likes= gameLike[i]
		max_likes_game=i 
	elif gameLike[i]== max_likes:
		if i < max_likes_game:
			max_likes_game=i

print(max_likes_game)
print(gameLike['football'])

