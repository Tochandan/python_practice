'''
Code Words
Description
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-..--...", (which is the concatenation "-.-." + ".-" + "-..."). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Input format
First line contains a positive integer n, denoting the number of test cases. It is followed by n lines. Each of the n lines contains space separated words.

Output format
n lines containing the number of different transformations among all words we have.

Sample input
1
gin zen gig msg
Sample output
2
Explanation
The transformation of each word is:

"gin" -> "--...-."

"zen" -> "--...-."

"gig" -> "--...--."

"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".

Note
The length of words will be at most 100000

Each words[i] will have length in range [1, 12].

words[i] will only consist of lowercase letters.
'''
# your code goes here
def trans(s):
	res=""
	result=[]
	code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
	for i in s:
	    if i!=" ":
	        res=res+str(code[ord(i)-97])
	    else:
	       res=res+" "
	lst=[str(i) for i in res.split()]
	
	for i in lst:
	    if i not in result:
	        result.append(i)
	return len(result)
	
		
for i in range(int(input())):
	s=input()
	print(trans(s))