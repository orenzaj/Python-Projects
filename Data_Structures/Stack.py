#from pythonds.basic.stack import Stack

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def reverse_string(mystr):
    return mystr[::-1]

def reverse_stack(mystr):
    stack = Stack()
    for ch in mystr:
        stack.push(ch)

    rev = ''
    while not stack.isEmpty():
        rev = rev + stack.pop()

    return rev


#print(reverse_string("hello"))
print(reverse_stack("hello"))