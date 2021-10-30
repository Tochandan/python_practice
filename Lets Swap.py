'''
Lets Swap
Y has a permutation p1,p2,p3.....pn of numbers from 1 to n.

Beautifulness of this permutation is defined as value of sum of abs(pi-i) for 1<=i<=n.

Y can swap two elements of the permutation at most once, what is the maximum beautifulness that Y can get?

Input
First line contains only n.

Second line contains the permutation p1,p2,p3...pn separated by space.

Output
The only line of output contains an integer, maximum beautifulness that Y can get.

Example
Input:

5

1 4 2 3 5

Output:

12

Explanation
Y can swap 1th and 5th element and the permutation becomes 5,4,2,3,1 with beautifulness . abs(5-1) + abs(4-2) + abs(2-3) + abs(3-4) + abs(1-5) = 12
'''
# 1)
# i                  =[1   2 3 4 5]
# arr                =[1   4 2 3 5]
# min(i,arr[i])      =[1   2 2 3 5(1)] =>max=5
# max(i,arr[i)       =[1(5) 4 3 4 5]=>min=1
# ans=0+2+1+1+0 =>   4+2*(max-min)
n=int(input())
arr=[int(x) for x in input().split()]
mini=[]
maxi=[]
ans=0
for i in range(n):
	ans+=abs(i+1-arr[i])
	mini.append(min(arr[i],i+1))
	maxi.append(max(arr[i],i+1))
ans+=2*(abs(max(mini)-min(maxi)))
print(ans)