# Week5Day3Lesson2 - Project 2 - Problem 1
# John Kowal  -  WALTER$

# STACK IMPLEMENTATION
# DO NOT MODIFY
class Stack(object):
    def __init__(self, list=None):
        if list is None:
            list = []
        self.stack = list

    def peek(self):

        if self.is_empty():
            return None
        return self.stack[-1]

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def push(self, data=None):
        self.stack.append(data)

    def print(self):
        print(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def clear(self):
        self.stack = []

    def __str__(self):
        return self.stack.__str__()

    def __repr__(self):
        return self.stack.__repr__()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.stack == other.stack
        return False

def flip(stack):
    f = Stack()  # Create a new stack
    while not stack.is_empty():
        f.push(stack.pop())
    return f

print('S', end="")
flip(Stack([1,2,3,4])).print()
