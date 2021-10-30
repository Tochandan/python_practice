'''
Print Movie Description -- Classes Practice Problems
Write a Movie class for which you can create movie objects. The objects should have the following variables: integer length_in_minutes, integer num_characters, string language. Each object should also have a run method which prints out: "This is a movie with characters and is minutes long."

Input
First line is a string, denoting the language of the movie Second line is an integer, denoting the number of characters Third line is an integer, denoting the length in minutes

Output
The output should be the return statement of run: "This is a movie with characters and is minutes long."

Example
Input:

French
4
200
Output:

This is a French movie with 4 characters and is 200 minutes long.
First line is French indicating the movie's language is French Second line is 4, indicating that the movie has 4 characters Third line is 200, indicating that the movie is 200 minutes long

'''
# your code goes here
class Movie:
	def __init__(self,language,num_characters,length_in_minutes):
		self.language=language
		self.num_characters=num_characters
		self.length_in_minutes=length_in_minutes
	def run(self):
	    print("This is a",self.language," movie with",self.num_characters,"characters and is",self.length_in_minutes,"minutes long.")
	   
language=input()
num_characters=int(input())
length_in_minutes=int(input())
ob1=Movie(language,num_characters,length_in_minutes)
ob1.run()