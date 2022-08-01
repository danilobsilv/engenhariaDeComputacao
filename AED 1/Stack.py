class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if (self.isEmpty) == True:
            print("The stack is empty")
        else:
            self.stack.pop()

    def top(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]

    def size(self):
        if len(self.stack) == 0:
            return None
        else:
            return len(self.stack)

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
