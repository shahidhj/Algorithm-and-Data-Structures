class QueueStack:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self,value):
        self.stack1.append(value)

    def pop(self,value):
        if not self.stack2:
            while(self.stack1):
                self.stack2.append(self.stack1.pop())
        self.stack2.pop()

    def peek(self):
        if self.stack2:
            return self.stack2[-1]
        return self.stack1[-1]

    def empty(self):
        return len(self.stack1)== 0 and len(self.stack2)== 0

