#if you prepend value of list u get reverse of list
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
        else:
            new_node=Node(value)
            new_node.next=self.head
            self.head=new_node
            return

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

lst=[1,2,3,4,5]
ll=LinkedList()
for i in lst:
    ll.append(i)
print("original")
ll.traverse()
print()
print("----------------------------------------------------------")
new_ll=LinkedList()
for i in lst:
    new_ll.prepend(i)
print("Reverse")
new_ll.traverse()