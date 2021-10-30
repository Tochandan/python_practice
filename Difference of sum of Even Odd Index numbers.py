'''
Difference of sum of Even Odd Index numbers
Write a function which takes a list of positive integers and returns the difference of sum of numbers and even and odd index positions.

Your function should take the list, sum all the numbers which are located at even index poistion of list and sum all the which are located at odd index poistion of list and subtract odd postion sum from even position sum.

you should name the function as difference_sum_even_odd_index and it should take a list.

Index of the list starts from 0.

If list has only one element, then sum of odd = 0

Input
list of positive intergers

Output
Integer

Example
Input:

[1,2,3,4,5,6]

Output:

-3
'''
# You should name your function as difference_sum_even_odd_index
# It should take a list of integers
# Return an integer
def difference_sum_even_odd_index(number):
    even=0
    odd=0
    for i in range(len(number)):
        if i%2==0:
            even=even+number[i]
        else:
            odd=odd+number[i]
    return (even-odd)

# Do not change anything below this line
if __name__ == "__main__":
    numbers = [int(i) for i in input().split(' ')]
    print(difference_sum_even_odd_index(numbers))