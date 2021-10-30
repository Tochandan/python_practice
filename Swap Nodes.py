'''
Swap Nodes
Given a singly linked list, write a function to swap elements pairwise.

Note:
This is a functional problem, so you don't need to worry about the input and output format. Simply take care of the swapNodes function.

Example & Explanation:
For example, if the linked list is 1->2->3->4->5 then the function should change it to 2->1->4->3->5.

Input : 1->2->3->4->5->6->NULL
Output : 2->1->4->3->6->5->NULL
Input : 1->2->3->4->5->NULL
Output : 2->1->4->3->5->NULL
Input : 1->NULL
Output : 1->NULL 
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

# Do not change anything above this line
    def swapNodes(self): 
        # YOU ONLY NEED TO COMPLETE THIS FUNCTION.
        temp=self.head
        if temp==None or temp.next==None:
        	return
        while temp!=None and temp.next!=None:
        	temp.data,temp.next.data=temp.next.data,temp.data #swap
        	temp=temp.next.next #move 2 
        return
        
  
  
    # Utility function to print the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data, end=" ")
            temp = temp.next


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

    llist.swapNodes()
    llist.printList()