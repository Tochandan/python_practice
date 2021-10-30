'''
Shape
Define a class named Rectangle:

It should have length and width as the properties.
It should have a method, named calculatePerimeter, which should return the perimeter of the rectangle.
It is given that, length and width will always be valid.
You don't need to worry about input/output and object of the class. The given template will take care of it.

The input will contain the length and width.

Input
One line containing two space seperated integers, denoting length and width respectively.

Output
Print perimeter of the given rectangle.

Example
Input1:

10 20
Output1:

60
'''
### Define the required class here...

class Rectangle:
    # Your code goes here
    def __init__(self,l,w):
    	self.l=l
    	self.w=w
    def calculatePerimeter(self):
    	return 2*(self.l+self.w)

### DO NOT CHANGE ANYTHING BELOW THIS LINE

if __name__ == '__main__':
    
    l, w = map(int, input().split())
    r1 = Rectangle(l, w)
    print(r1.calculatePerimeter())