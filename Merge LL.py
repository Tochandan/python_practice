'''
Merge LL
Description
Given 2 sorted LL You need to merge them.

You just need to complete mergeLists function

Input
First line contains an integer N1 denoting the size of the 1st Linked List.

Second line contain N1 space separated integers dentoing the LL.

Third line contain an integer N2 denoting the size of 2nd LL.

Second line contain N2 space separated integers dentoing the LL.

Output
Print the mergerd list

Input:

3

2 3 5

4

1 4 6 7

Output:

1 2 3 4 5 6 7
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
    before = None
    current = llist.head
    if current is None:
        return
    after = current.next
    while after:
        current.next = before
        before = current
        current = after
        after = after.next
    current.next = before
    llist.head = current
 
 
def mergeLists(headA, headB):
	ans=None
	if headA.data<headB.data:
		head=Node(headA.data)
		ans=head
		headA=headA.next
	else:
		head=Node(headB.data)
		ans=head
		headB=headB.next
	while headA and headB:
		if headA.data<headB.data:
			ans.next=Node(headA.data)
			ans=ans.next
			headA=headA.next
		else:
			ans.next=Node(headB.data)
			ans=ans.next
			headB=headB.next
	while headA:#if headA has left over values
		ans.next=Node(headA.data)
		ans=ans.next
		headA=headA.next
	while headB:
		ans.next=Node(headB.data)
		ans=ans.next
		headB=headB.next
	return head	
	
	

# Create 2 lists
listA = LinkedList()
listB = LinkedList()
 
# Add elements to the list in sorted order
n1 = int(input())
l1 = list(map(int, input().split(' ')))
n2 = int(input())
l2 = list(map(int, input().split(' ')))
for i in l1:
    listA.append(i)
for i in l2:
    listB.append(i)
# Call the merge function
listA.head = mergeLists(listA.head, listB.head)
 
# Display merged list
listA.display()