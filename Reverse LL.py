'''
Reverse LL
Description
Given pointer to the head node of a linked list, the task is to reverse the linked list. We need to reverse the list by changing the links between nodes.

You just need to implement the reverse_llist function.

Input
First line contains an integer N denoting the size of the Linked List.

Next line contain N space separated integers dentoing the LL.

Output
Print the reversed LL

Input:

5

1 2 3 4 5

Output:

5 4 3 2 1
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next
 
 
def reverse_llist(llist):
    # Implement this
    curr=llist.head
    prev=None
    next=None
    while curr!=None:
    	next=curr.next  #store the adress of next
    	curr.next=prev #breaking and making of reverse bond
    	prev=curr
    	curr=next
    	#prev is having the head of reverse ll
    llist.head=prev
 
 
a_llist = LinkedList()
n = int(input())
l = list(map(int, input().split(' ')))
# data_list = input('Please enter the elements in the linked list: ').split()
for data in l:
    a_llist.append(int(data))
 
reverse_llist(a_llist)
a_llist.display()