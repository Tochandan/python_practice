'''
Grovlye String
Trico is trying to impress a girl. But the girl is not showing any sign of interest to him. So his best friend suggested him to gift one Grovyle string to her. Grovlye string is a odd length string consisting of only lowercase alphabets arranged in such a way that a number Y associated with it is smallest as possible.

Y is calculated as : First take absolute distance of each character's position from the center of the string i.e., (string length/2) and then multiply the distance with its ASCII value. Similarly find all the values and add them.

Example : Given string : aaa

Here only one unique permutation is possible : aaa

distances are : for first a, d1 = 1, second a, d2 =0, third a, d3 = 1;

so Y = 1 X 97 + 0 X 97 + 1 X 97 = 194;

So given a string of odd length consisting of only lowercase alphabets, find one permutation of the given string such that Y is smallest as possible. And if there are many such strings then print the lexicographically smallest one.

Input
First line contains T, the number of test cases that follow. Next T lines, each contains one odd length string consisting of only lowercase alphabets.

Output
For each test case, print the desired result in separate lines.

Constraints:
1 ≤ T ≤ 1000
0 ≤ String Length ≤ 1001
Example
Input:

2

aaa

abc

Output:

aaa

acb

Explanation:
In the second test case, the Y value is: 1 X 97 + 0 X 99 + 1 X 98 = 195, which is the minimum possible out of all the combinations of the given letters.
'''
# your code goes here
for i in range(int(input())):
	s=input()
	ss=[i for i in s]
	ss.sort()
	s="".join(ss)
	k=len(s)-1
	i=(len(s)-1)//2
	j=(len(s)-1)//2
	ss[i]=s[k]
	k-=1
	i-=1
	j+=1
	while(i>=0 and j<len(s)):
		ss[j]=s[k]
		k-=1
		j+=1
		ss[i]=s[k]
		k-=1
		i-=1
	print("".join(ss))