from node import Node


class Stack:

    def __init__(self):
        self.top = None
        self.list = []
    def push(self, item):
        new_node = Node(item)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        return self

    def pop(self):
        if self.top is None:
            return 'this stack is empty'
        else:
            temp = self.top.value
            self.top = self.top.next
        return temp
