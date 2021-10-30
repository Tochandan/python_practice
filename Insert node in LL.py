'''
Insert node in LL
Create a link list of size N according to the given input literals. Each integer input is accompanied by an indicator which can either be 0 or 1. If it is 0, insert the integer in the beginning of the link list. If it is 1, insert the integer at the end of the link list.

Input
First line is an integer T, representing total number of test cases. For each testcase, 1st line containing space separated integers of linked list and indicator to insert from left to right.

Output
T lines, each line containing the nodes of linked list for each test case.

Example
Input: 1

1 0 2 1 3 0

Output: 3 1 2

Explanation
For the first test case, insert 1 ,indicator 0 so insert at begining, linked list is 1 insert 2 ,indicator 1 so insert at end, linked list is 1 2 insert 3 ,indicator 0 so insert at begining, linked list is 3 1 2
'''
class Node: 
    def __init__(self, value): 
        self.data = value 
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_value): 
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
          
    def makeListAndPrint(self):
        #####WRITE CODE HERE####
        ll=LinkedList()
        ll.head=None
        ll.tail=None
        temp1=self.head
        while temp1!=None:
        	if int(temp1.next.data)==0:
        		#temp1.data should be inserted at beginning.
        		currentLL=ll.head
	        	ll.head=Node(int(temp1.data))
	        	if currentLL is None:
	        		ll.tail=ll.head
	        	ll.head.next=currentLL
	        else:
	        	#temp1.data should be inserted at end
	        	ll.push(int(temp1.data))
	        temp1=temp1.next.next
        p=ll.head
        while p!=None:
            print(p.data,end=" ")
            p=p.next
        return
            
        

def read_list_input():
    vals = input().split(' ')
    linkedList = LinkedList() 
    for val in vals:
        linkedList.push(val)
    return linkedList

test_cases = int(input())
for i in range(test_cases):
    linkedList = read_list_input()
    linkedList.makeListAndPrint()