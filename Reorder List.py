'''
Reorder List
Given a singly linked list.

L: L0 -> L1 -> ... -> Ln-1 -> Ln
Reorder it to:

L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
You must do this in-place without altering the nodes’ values. In-place means without using extra space i.e., O(1) space.

Note:
This is a functional problem, so you don't need to worry about the input and output format. Simply take care of the reorderList function.

Example:
1) Given a linked list: 1 -> 2 -> 3 -> 4, reorder it to 1 -> 4 -> 2 -> 3

2) Given a linked list: 1 -> 2 -> 3 -> 4 -> 5, reorder it to 1 -> 5 -> 2 -> 4 -> 3
'''
# Node class 
class Node: 

	# Constructor to initialize the node object 
	def __init__(self, data): 
		self.data = data 
		self.next = None

class LinkedList:
# Function to initialize head 
    def __init__(self): 
        self.head = None

    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data, end=" ")
            temp = temp.next

# Do not change anything above this line

    def reorderList(self):
        # YOU ONLY NEED TO COMPLETE THIS FUNCTION.
        def reverseLL(h):
        	curr=h
        	prev=None
        	while curr !=None:
        		next=curr.next
        		curr.next=prev
        		prev=curr
        		curr=next
        	return prev
        	
        A=self.head
        l=0
        while A:
        	l+=1
        	A=A.next
        	
        mid=self.head
        for i in range(l//2):
        	mid=mid.next
        B=reverseLL(mid.next) # mid half
        mid.next=None         # to seperate first half and second half
        A=self.head
        while B:
        	nextA=A.next
        	A.next=B
        	
        	nextB=B.next
        	B.next=nextA
        	A=nextA
        	B=nextB
        return self.head


# Do not change anything below this line
if __name__ == '__main__':
    
    n = int(input())

    # Start with the empty list 
    llist = LinkedList() 

    temp = [int(x) for x in input().split()]

    if(n<1):
        llist.head = None
    elif(n<2):
        llist.head = Node(temp[0])
    else:
        llist.head = Node(temp[0])
        second = Node(temp[1])
        llist.head.next = second
        curr = llist.head.next


    for i in range(2,n):
        t = Node(temp[i])
        curr.next = t
        curr = curr.next

    llist.head = llist.reorderList()
    llist.printList()