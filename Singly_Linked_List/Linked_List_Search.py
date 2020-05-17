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
            print(cur_node.value,end=" ")
            cur_node=cur_node.next
        return

    def Search(self,value):
        if self.head is None:
            return None

        node=self.head
        while node:
            if node.value==value:
                return True
            node=node.next
        return False

ll=LinkedList()
ll.prepend(10)
ll.prepend(20)
ll.prepend(30)
ll.prepend(40)
ll.prepend(50)
print("Content : ")
ll.traverse()
print()
val=60
print(f"val={val}")
print(ll.Search(val))