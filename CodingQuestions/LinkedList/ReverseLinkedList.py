class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#Iterative method
class LinkedList:
    def __init__(self):
        self.head=None

    #function to reverse the linked list

    def reverse_linkedlist(self):
        prev=None
        current=self.head
        while current is not None:
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev

    #push function, so that while testing doesn't have to write next.next
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    #printing the linkedlist

    def print_linkedlist(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next

#Driver code
llist=LinkedList()
llist.push(20)
llist.push(30)
llist.push(40)
llist.push(50)


print ("-----------------current linked list----------------")
llist.print_linkedlist()
print ("-----------------reverse linked list----------------")
llist.reverse_linkedlist()
llist.print_linkedlist()

