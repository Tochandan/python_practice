'''
Negativity factor of a linked list
You are given a Linked list of integers(both positive and negative). Complete the "Negativity" method which finds the negativity factor of the linked list. Negativity factor of the linked list is defined as the percentage of elements of linked list that are negative.

i.e (number of negative elements / Total number of elements)*100

Print only the integer part of the Negativity factor finally.

You dont need to implement your own linked list from scratch, just complete the 'Negativity' function given in the template below. Also you dont need to worry about taking the input.

Example
Lets say the linked list in the input was

1->-2->3->-4->1->2

then the expected output will be

33

as total negative elements =2 (-2,-4)

total elements=6

Negativity = (2/6)*100 = 33.333333 -> 33
'''
class Node:
    def __init__(self, key):
        self.data = key
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    @staticmethod
    def insert_node(val, current):
        temp = Node(val)
        current.next = temp
        current = current.next
        return current
    
    #complete the function given below
    @staticmethod
    def Negativity(List):
    	neg=0
    	total=0
    	temp=List.head
    	while temp!=None:
    		if  temp.data<0:
    			neg+=1
    		total+=1
    		temp=temp.next
    	return int((neg/total)*100)
    		


ll = LL()
num = [int(i) for i in input().split("->")]
ll.head = Node(num[0])
curr = ll.head
for i in num[1:]:
    curr = LL.insert_node(i, curr)
print(LL.Negativity(ll))