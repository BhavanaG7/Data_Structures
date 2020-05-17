class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def prepend(self,value):
        if self.head is None:
            self.head=Node(value)
            return
        new_head=Node(value)
        new_head.next=self.head
        self.head=new_head


    def traverse(self):
        cur_node=self.head
        while cur_node:
            print(cur_node.value)
            cur_node=cur_node.next
        return

lst=[10,20,30,40]
ll=LinkedList()
for i in lst:
    ll.prepend(i)
ll.traverse()