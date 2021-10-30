'''
reverse-dll
Given a doubly linked lists, your task is to complete the function reverse() which should reverse the doubly linked list.

A Doubly Linked List (DLL) contains an extra pointer, typically called previous pointer, together with next pointer and data which are there in singly linked list. A DLL can be traversed in both forward and backward direction. 
Note:
This is a functional problem, so you don't need to worry about the input and output format. Simply take care of the reverse function.
The head node might be None to indicate that the list is empty.
Function Description
Complete the reverse function in the editor.

Return:

DoublyLinkedListNode: a reference to the head of the reversed list
Example & Explanation:
Input:

DLL : 1 <-> 2 <-> 3 <-> 4 <-> 5

Reversed DLL : 5 <-> 4 <-> 3 <-> 2 <-> 1
'''
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
 
 
class DoublyLinkedList:
     # Constructor for empty Doubly Linked List
    def __init__(self):
        self.head = None
 
 # DO NOT CHANGE ANYTHING ABOVE THIS LINE

    # Function to reverse a Doubly Linked List
    def reverse(self):
    	temp = None
    	current = self.head
    	while current is not None:
    		temp = current.prev
    		current.prev = current.next
    		current.next = temp
    		current = current.prev
    	if temp is not None:
    		self.head = temp.prev
        

 # DO NOT CHANGE ANYTHING BELOW THIS LINE
 
    # Given a reference to the head of a list and an
    # integer,inserts a new node on the front of list
    def push(self, new_data):
 
        # 1. Allocates node
        # 2. Put the data in it
        new_node = Node(new_data)
 
        # 3. Make next of new node as head and
        # previous as None (already None)
        new_node.next = self.head
 
        # 4. change prev of head node to new_node
        if self.head is not None:
            self.head.prev = new_node
 
        # 5. move the head to point to the new node
        self.head = new_node
 
    def printList(self, node):
        while(node is not None):
            print(node.data, end=' ')
            node = node.next
 
 
# Driver code
for _ in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]
    
    dll = DoublyLinkedList()
    for idx in range(len(arr)-1, -1, -1):
        dll.push(arr[idx])

    dll.reverse()
    dll.printList(dll.head)
    print()