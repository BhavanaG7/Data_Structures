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
            self.tail=self.tail.next
        return

    def traverse(self):
        cur_node=self.head
        while cur_node:
            print(cur_node.value)
            cur_node=cur_node.next
        return

lst=[1,2,3,4,5,6]
ll=LinkedList()
for i in lst:
    ll.append(i)
ll.traverse()
