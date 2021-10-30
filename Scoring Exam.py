'''
Scoring Exam
Milly is at the examination hall where she is reading a question paper. She checked the question paper and discovered that there are N questions in that paper. Each question has some score value. Ideally it's like questions requiring more time have more score value and strangely no two questions on the paper require same time to be solved.

She is very excited by looking these questions. She decided to solve K questions while maximizing their score value. Could you please help Milly to determine the exact time she needs to solve the questions.

Input
First line of input contains two space separated integers N and Q, where N is the number of questions available and Q is number of queries

Next line contains N space separated integers denoting the time Ti of N questions

Next line contains N space separated integers denoting the scores Si of N questions

Next Q lines contains a number K each, the number of questions she wants to solve

Output
Print the time required for each query in a separate line.

Example
Input:

5 2

2 3 9 4 5

3 5 11 6 7

5

3

Output:

23

18
'''
n,query=map(int,input().split())
time=list(map(int,input().split()))
score=list(map(int,input().split()))

score.sort(reverse=True)
time.sort(reverse=True)

k=[]
x=0
for i in range(n):
    x=x+time[i]
    k.append(x)
for i in range(query):
    print(k[int(input())-1])