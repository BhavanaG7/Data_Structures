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

    #insert at specified position
    def insert(self,value,pos):
        target=Node(value)
        if self.head is None:
            self.head=target
            target=self.head
            return
        #find previous node position
        def getPrev(pos):
            temp=self.head
            count=1
            while count<pos:
                temp=temp.next
                count+=1
            return temp

    #5>1->3->7
    #5->1->2->3->7
    #getPrev->gets us 1
    #prev=1
    #prev.next=2
    #next_node=3
        prev=getPrev(pos)
        next_node=prev.next
        prev.next=target
        target.next=next_node

    def prepend(self,value):
        if self.head is None:
            self.head=Node(value)
            return
        new_head=Node(value)
        new_head.next=self.head
        self.head=new_head
        return

    def traverse(self):
        linked_list=""
        if self.head is None:
            print("Empty linked list")
        else:
            cur_node=self.head
            while cur_node:
                linked_list+=str(cur_node.value)+ " "
                cur_node=cur_node.next
            print(linked_list)

ll=LinkedList()
l=[5,1,3,7]

for i in l:
    ll.append(i)

ll.traverse()
ll.insert(10,2)
ll.traverse()