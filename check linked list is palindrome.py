'''
check linked list is palindrome
Given a singly linked list of integers, write a function that returns true if the given list is a palindrome, else false.

Input
First line is an integer T, representing total number of test cases. For each testcase, 1st line containing space separated integers of linked list from left to right.

Output
T lines, each line containing the result for each test case.

Example
Input: 2

1 2 2 1

1 1 1 1 2

Output: True

False

Explanation
For the first test case, 1 2 2 1 back walk also gives 1 2 2 1 so true

For the second test case, 1 1 1 1 2 back walk gives 2 1 1 1 1 so not same, will give output false
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
          
    def isPalin(self):
        #####WRITE CODE HERE####
        def reverse(h):
        	curr=h
        	prev=None
        	next=None
        	while curr!=None:
        		next=curr.next #store adress of next
        		curr.next=prev  #breaking and making reverse bond
        		#pointer movement
        		prev=curr
        		curr=next
        	return prev # prev is having hewad of reverse ll
        l=0
        temp=self.head
        while temp!=None:
            l+=1
            temp=temp.next
        mid=l//2
    #get second half of ll
        temp=self.head
        for i in range(mid-1):
            temp=temp.next
    	#separating two of ll 
        secondhalf=temp.next
        temp.next=None
        secondhalf=reverse(secondhalf)
    #comparing first half and reverse of second half
        temp1,temp2=self.head,secondhalf
        while temp1!=None and temp2!=None:
            if temp1.data != temp2.data:
                return False
            temp1=temp1.next
            temp2=temp2.next
        return True
        

def read_list_input():
    vals = input().split(' ')
    linkedList = LinkedList() 
    for val in vals:
        linkedList.push(val)
    return linkedList

test_cases = int(input())
for i in range(test_cases):
    linkedList = read_list_input()
    print(linkedList.isPalin())