class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def remove_nth_element(self, position):
        first_node = Node(0)
        first_node.next = self.head
        first = first_node
        second = first_node

        for i in range(1, position + 2):  # as we have to go N+1
            first = first.next

        while first is not None:
            first = first.next  # this first is present in N+1 from the head node
            second = second.next

        second.next = second.next.next  # here cursor is at the nth element , we just have to move one element forward

        return first_node.next  # again the start og the LL.
