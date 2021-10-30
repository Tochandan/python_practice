'''
Prime queries
A prime number is defined as a number-

which is not divisible by any number except 1 and itself.
Smallest prime number is 2.
User makes Q queries, in each query a number is supplied. For each query, Count the number of prime numbers smaller than or equal to the query number. User also keeps a limit on the maximum number that can be provided in any of the query, which is given in the input.

Constraints
1<= Maximum Query number(Nmax)<= 100000

1<= number of queries<= 100000

Input
First line of the input contains two integers first representing the maximum query number(Nmax) and the number of queries(Q) respectively. Following Q lines contains an integer each representing the query number(N<= Nmax).

Output
For each query print the number of prime numbers smaller than or equal to the number.

Example
Input:

20 5

3

11

16

1

19

Output:

2

5

6

0

8

Explanation:

Primes less than equals 3 -> 2,3

Primes less than equals 11 -> 2,3,5,7,11

Primes less than equals 16 -> 2,3,5,7,11,13

Primes less than equals 1 -> No such number

Primes less than equals 19-> 2,3,5,7,11,13,17,19

Note that 20 provided in the first line of the input makes sure that user wont provide any input >20.
'''
# 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
# 0,0,1,1,0,1,0,1,0,0,0,1,0,1,
n,q=map(int,input().split())
prime=[1 for i in range(n+1)]
prime[0],prime[1]=0,0
p=2
while p*p<=n:
	if prime[p]==1:
		for i in range(p*p,n+1,p):
			prime[i]=0
	p+=1
for i in range(1,len(prime)):
	prime[i]+=prime[i-1]
for i in range(q):
	query=int(input())
	print(prime[query])
	
		