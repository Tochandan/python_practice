'''
Cut Rope
You are given N ropes. A cut operation is performed on ropes such that all of them are reduced by the length of the smallest rope. Display the number of ropes left after every cut operation till the length of each rope is zero.

Input
The first line of input contains integer N denoting the number of ropes. Next N lines denotes N elements(length of rope).

Output
Print the resultant array, one element in one line.

Constraints:
1 ≤ N ≤ 100000
Example
Input:

6

5

1

1

2

3

5

Output:

4

3

2

Explnation:
5 1 1 2 3 5

After first iteration of cutting

4 1 2 4 -> 4

2nd iteration

3 1 3 -> 3

3rd iteration

2 2

After that they become 0

So, answer is 4 3 2
'''
def cutRope(A):
    # Complete this function
    A.sort()
    n=len(A)
    operation=0
    cuttingLength=A[0]
    ans=[]
    for i in range(1,n):
    	if(A[i]>cuttingLength):
    		ans.append(n-i)
    	cuttingLength=A[i]
    	operation +=1
    if (operation==0):
    	ans.append(0)
    return ans
    

# Do not change anything below this line
if __name__ == '__main__':
    input_numbers = []
    for _ in range(int(input())):
        input_numbers.append(int(input()))

    for i in cutRope(input_numbers):
        print(i)