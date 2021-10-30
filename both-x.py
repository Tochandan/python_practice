'''
both-x
Description
Given two strings (string1 and string2) and a number x, return a list of all the characters that appear exactly x times in both the strings (in sorted order). Ignoring the case.

Input format
First line denotes t, denoting the number of testcases. Each test case contains 3 space seperated elements in one line, denoting string1 , string2 and x respectively.

Output format
One line for each test case.

Sample input
1
Sample Pampe 1
Sample output
a e m
Explanation
a, m, e (all the 3 chars appear exactly once in both the strings).
'''
def bothCountX(string1, string2, x):
    
    # Complete this function, and return the list of resultant characters in sorted order
    # n=max(len(string1),len(string2))
    lst=[]
    
    for i in string1:
        if i in string2:
            z=i
            z.swapcase()
            if string2.count(i)== x and string2.count(z)==x:
                lst.append(i)
    lst.sort()
    return lst

for _ in range(int(input())):
    string1, string2, x = input().split()
    x = int(x)
    print(*bothCountX(string1, string2, x))