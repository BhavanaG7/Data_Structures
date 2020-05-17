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

    def size(self):
        size=0
        if self.head is None:
            return 0
        else:
            cur_node=self.head
            while cur_node:
                size+=1
                cur_node=cur_node.next
            return size

ll=LinkedList()
lst=list(map(int,input().rstrip().split()))

for val in lst:
    ll.append(val)

print(ll.size())      