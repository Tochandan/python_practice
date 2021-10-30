'''
Game of Strength
Andrew is very fond of Maths.He has N boxes with him,in each box there is some value which represents the Strength of the Box.The ith box has strength A[i]. He wants to calculate the Overall Power of the all N Boxes.

Overall Power here means Sum of Absolute Difference of the strengths of the boxes(between each pair of boxes) multiplied by the Maximum strength among N boxes. Since the Overall Power could be a very large number,output the number modulus 10^9+7(1000000007).

Input
First line of the input contains the number of test cases T. It is followed by T test cases. Each test case has 2 lines. First line contains the number of boxes N. It is followed by a line containing N elements where ith element is the strength of Andrew's ith box.

Output
For each test case, output a single number, which is the Overall Power for that testcase.

Example
Input:

2

2

1 2

5

4 5 3 1 2

Output:

2

100
'''
# your code goes here

#strength [4 5 3 1 2]

#4-> (5, 3, 2, 1) 
#5-> (3, 1, 2)
#3-> (1, 2)
#1-> (2)
# 2->.
#SORTED reverse
#strength [5 4 3 2 1]
#(odd length)

# [5*(4)-4-3-2-1] + [4*(3)-3 - 2- 1] + [3*(2)-2-1] [2-1] 
#5 *(4) + 4* (2) + 3* (0) + 2*(-2) + 1*(-4) 
# Pattern is->n-1 to -(n-1)

#strength [4 3 2 1] (even length)

# [4* (3)-4-3-2-1] + [3*(2) -2 - 1] + [2-1]

#4 *(3) + 3*(1) + 2*(-1) + 1*(-3) 
#pattern is -> n-1 to -(n-1)


def game(arr,n):
	arr.sort(reverse=True)
	res=0
	m=n-1
	for i in arr:
		res+=i*m
		m-=2
	return ((res%(1000000007))*(max(arr)%1000000007))%1000000007
    
test=int(input())
for i in range(test):
	n=int(input())
	arr=list(map(int,input().strip().split()))[:n]
	print(game(arr,n))