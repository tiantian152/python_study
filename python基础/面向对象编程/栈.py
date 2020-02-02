class Stack():
    def __init__(self):
        self.stack = []

    def push(self,value):
        self.stack.append(value)
        return True

    def pop(self):
        #先判断栈是否为空
        if self.stack:
            item = self.stack.pop()
            return item
        else:
            return False

    def get_top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return False

    def length(self):
        return len(self.stack)

    def view(self):
        return ','.join(self.stack)


s = Stack()
s.push('1')
s.push('2')
print(s.length())
item = s.pop()
print(item)
print(s.view())