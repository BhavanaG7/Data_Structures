class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

    def get_value(self):
        return self.value

    def set_value(self,value):
        self.value=Node(value)

    def set_left_child(self,value):
        self.left=Node(value)

    def get_left_child(self):
        return self.left

    def set_right_child(self,value):
        self.right=Node(value)

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        if self.left:
            return True
        return False

    def has_right_child(self):
        if self.right:
            return True
        return False
    
    def __str__(self):
        return f"Node({self.get_value()})"

    def __repr__(self):
        return f"Node({self.get_value()})"

class Tree(object):
    def __init__(self,value=None):
        self.root=Node(value)

    def get_root(self):
        return self.root

tree=Tree("D")
tree.get_root().set_left_child("B")
tree.get_root().set_right_child("E")
tree.get_root().get_left_child().set_left_child("A")
tree.get_root().get_left_child().set_right_child("C")
tree.get_root().get_right_child().set_right_child("F")

def pre_order_traverse(tree):
    visit_order=list()
    root=tree.get_root()

    def traverse(node):
        if node:
            #VALUE
            visit_order.append(node.get_value())
            #left
            traverse(node.get_left_child())
            #right
            traverse(node.get_right_child())
    traverse(root)
    return visit_order

print("Pre-Order Traversal")
print(pre_order_traverse(tree))

def in_order_traverse(tree):
    visit_order=list()
    root=tree.get_root()

    def traverse(node):
        if node:
            #left
            traverse(node.get_left_child())
            #value
            visit_order.append(node.get_value())
            #right
            traverse(node.get_right_child())
    traverse(root)
    return visit_order

print("In-Order Traversal")
print(in_order_traverse(tree))

def post_order_traverse(tree):
    visit_order=list()
    root=tree.get_root()

    def traverse(node):
        if node:
            #left
            traverse(node.get_left_child())
            #RIGHT
            traverse(node.get_right_child())
            #value
            visit_order.append(node.get_value())
    traverse(root)
    return visit_order

print("Post-Order Traversal")
print(post_order_traverse(tree))