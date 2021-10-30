'''
Count Pairs
Given two linked lists, your task is to complete the function countPairs(), which returns the count of all pairs from both lists whose sum is equal to the given value X. (All the values in each Linked List will be distinct.)

The 2 numbers of a pair should be parts of different lists.

Note:
This is a functional problem, so you don't need to worry about the input and output format. Simply take care of the countPairs function.

Return 0 if no such pairs exists.

Example & Explanation:
Input:

L1 = 1->2->3->4->5->6
L2 = 11->12->13
X = 15
Output: 3 Explanation: There are 3 pairs that add up to 15 : (4,11) , (3,12) and (2,13)

Input:

L1 = 7->5->1->3
L2 = 3->5->2->8
X = 10
Output: 2 Explanation: There are 2 pairs that add up to 10 : (7,3) and (5,5)
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

    def countPairs(self, head2, x):
        # YOU ONLY NEED TO COMPLETE THIS FUNCTION.
        set1=set()
        temp1=self.head
        while temp1!=None:
        	set1.add(temp1.data)
        	temp1=temp1.next
        temp2=head2
        count=0
        while temp2!=None:
        	#A+B=X =>X-B
        	if (x-temp2.data) in set1:
        		count +=1
        	temp2=temp2.next
        return count
        


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

    # For 2nd linked list:
    m = int(input())

    # Start with the empty list 
    llist2 = LinkedList() 

    temp = [int(x) for x in input().split()]

    if(m<1):
        llist2.head = None
    elif(m<2):
        llist2.head = Node(temp[0])
    else:
        llist2.head = Node(temp[0])
        second = Node(temp[1])
        llist2.head.next = second
        curr = llist2.head.next


    for i in range(2,m):
        t = Node(temp[i])
        curr.next = t
        curr = curr.next

    print(llist.countPairs(llist2.head, int(input())))