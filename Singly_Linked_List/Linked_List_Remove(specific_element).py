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
            return

        else:
            self.tail.next=Node(value)
            self.tail=self.tail.next
            return

    def traverse(self):
        cur_node=self.head

        while cur_node:
            print(cur_node.value,end=" ")
            cur_node=cur_node.next
        return

    def remove(self,value):
        if self.head is None:
            return 
        if self.head.value==value:
            self.head=self.head.next
            return

        cur_node=self.head
        while cur_node.next:
            if cur_node.next.value==value:
                cur_node.next=cur_node.next.next
                return
            cur_node=cur_node.next
        print("Value not found")

lst=[1,2,3,4,5,6]
ll=LinkedList()
for i in lst:
    ll.append(i)
ll.traverse()
print()
ll.remove(2)
ll.traverse()