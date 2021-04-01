class Stack:

    def __init__(self):
        self.list_stack = []

    def push(self, item):
        self.list_stack.append(item)

    def pop(self):
        return self.list_stack.pop(-1)
