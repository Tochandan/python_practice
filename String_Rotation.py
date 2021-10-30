'''
String_Rotation
Description:
Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat" "backyard" is a rotation of "kyardbac" "cheese" is a rotation of "eesech" "useho" is a rotation of "house")

Note: The function isSubstring() has already been provided to you. You can directly use that function without having to write the function again yourself. Use that function to check if a string is a rotation of another string. You have to compulsorily use the isSubstring function. Do not directly check for rotation between the two strings s1 and s2. You just need to complete the isRotation function.

Input Format:
The first line of the input contains an integer t denoting the number of test cases. Each of the next two lines contains a string each. Please keep in mind both s1 and s2 will be of the same length.

Output Format:
Return True or False depending on whether s2 is a rotation of s1.

Sample Case:
Input
2 
waterbottle 
erbottlewat 
cat 
dog
Output
True
False
'''
def isSubstring(s1, s2):
    if s1.find(s2) != -1:
        return True
    if s2.find(s1) != -1:
        return True
    return False

## Do not change anything above
def isRotation(s1,s2):
    ## You can only call isSubstring function from this function once. Use this function to check if s2 is a rotation of s1.
    s2+=s2
    if(isSubstring(s1,s2)):
    	print(True)
    else:
    	print(False)
    	
    
## Do not change anything below
t = int(input()) 
for i in range(t):
    s1 = input() 
    s2 = input()
    isRotation(s1,s2)