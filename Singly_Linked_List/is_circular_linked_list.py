class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def append(self,value):
        if self.head is None:
            self.head=Node(value)
            self.tail=self.head

        else:
            self.tail.next=Node(value)
            self.tail=self.tail
        return


def has_cycle(linked_list):
    if linked_list.head is None:
        return False

    slow=linked_list.head
    fast=linked_list.head

    while fast and fast.next:
        #move slow ahead by 1 node
        slow=slow.next

        #move fast ahead by 2 node
        fast=fast.next.next

        if slow==fast:
            return True

    return False
      