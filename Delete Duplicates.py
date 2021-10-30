'''
Delete Duplicates
Description
Given an unsorted linked list of N nodes. The task is to remove duplicate elements from this unsorted Linked List. When a value appears in multiple nodes, the node which appeared first should be kept, all others duplicates are to be removed. You need to implement remove duplicates function only.

Input
First line contains an integer N denoting the size of the Linked List.

Next line contain N space separated integers dentoing the LL.

Output
Print the final LL

Input:

5

1 1 2 2 5

Output:

1 2 5
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
 
    def get_prev_node(self, ref_node):
        current = self.head
        while (current and current.next != ref_node):
            current = current.next
        return current
 
    def remove(self, node):
        prev_node = self.get_prev_node(node)
        if prev_node is None:
            self.head = self.head.next
        else:
            prev_node.next = node.next
 
    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next
 
# Implement this Function 
def remove_duplicates(llist):
	#valid for sorted as well as unsorted
	track=set()
	temp=llist.head
	if temp==None:
		return
	track.add(temp.data)#adding the first value in the set
	while temp.next!=None:
		if temp.next.data in track:
			temp.next=temp.next.next #temp.next fdeleted
		else:
			track.add(temp.next.data)
			temp=temp.next
	return
	
	
 
 
a_llist = LinkedList()
 
n = int(input())
l = list(map(int, input().split(' ')))
for data in l:
    a_llist.append(data)
 
remove_duplicates(a_llist)
 
a_llist.display()