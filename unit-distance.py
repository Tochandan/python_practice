'''
unit-distance
Description
Check if edit distance between two strings is one or not. If its one, print True else False. Number of edits done to the string a to get string b is called the edit distance.

An edit between two strings is one of the following changes:

- Add a character
- Delete a character
- Change a character
Note:
The strings are case sensitive, and they may also contain symbols or numbers.
Input format
First line denotes t, denoting the number of testcases. Each test case contains two space seperated strings in one line.

Output format
One line for each test case.

Sample input
2
peaks peeks
bbbbb bbbbb
Sample output
True
False
Explanation
Number of edits in first case is 1, hence True. (The edit is to change the 3rd character of first string 'a' to 'e', or vice versa)
Number of edits in first case is 0, hence False.
'''
def isEditDistanceOne(string1, string2): 
    # Complete this function, and return True/False
    n=len(string1)
    m=len(string2)
    if (abs(n-m)>1 or string1==string2):
    	return False
    edit_dist=0
    i=0
    j=0
    while(i<n and j<m):
    	if string1[i]== string2[j]:
    		i+=1
    		j+=1
    	elif edit_dist==1:
    		return False
    	else:
    		edit_dist=1
    		if n>m:
    			i+=1
    		elif m>n:
    			j+=1
    		else:
    			i+=1
    			j+=1
    			
    return True
    				
    			

for _ in range(int(input())):
    input_string1, input_string2 = input().split()
    print(isEditDistanceOne(input_string1, input_string2))