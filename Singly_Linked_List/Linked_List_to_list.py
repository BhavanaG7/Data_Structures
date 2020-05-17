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

    def ll_to_list(self):
        new_list=[]

        cur_node=self.head
        while cur_node:
            new_list.append(cur_node.value)
            cur_node=cur_node.next
        return new_list

ll=LinkedList()
ll.append(20)
ll.append(40)
ll.append(60)
ll.append(80)
ll.append(100)

print(ll.ll_to_list())