'''
prime checker function
Write a function that takes a positive integer n and returns either True or False. It should return True when n is prime and False whenn` is not prime.

Input
One positive integer N

Output
One Boolean, denoting whether or not the given N is prime

Example
You have fill in a function. That function takes N as input

Input:

def is_prime(number)

Output:

Function should return True or False
'''
## Following function takes integer and should return True if it's prime 
## otherwise  should return False.
def is_prime(input_number):
    if input_number==2:
        return True
    elif input_number>2:
    
        for i in range(2, int(input_number/2)+1):
      
            if (input_number % i) == 0:
                return False
                break
        else:
            return True
      
    else:
        return False




### Please don't change anything below this line.
if __name__ == "__main__":
    number = int(input())
    print(is_prime(number))
    
