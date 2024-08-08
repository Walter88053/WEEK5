# Week5Day3Lesson4 - Project 2 - Problem 3
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

class Queue(object):
    def __init__(self, list=None):
        if list is None:
            list = []
        self.queue = list

#    def get_list(self):
#        return self.queue

    def size(self):
        return len(self.queue)

    def front(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def tail(self):
        return self.queue[-1]

    def deq(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def enq(self, data=None):
        self.queue.append(data)

    def print(self):
        print(self.queue)

    def __str__(self):
        return self.queue.__str__()

    def __repr__(self):
        return self.queue.__repr__()

    def is_empty(self):
        return len(self.queue) == 0

    def clear(self):
        self.queue = []

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.queue == other.queue
        return False

def main():
    q = Queue()
    q.print()
    print("Is empty?", q.is_empty())
    for i in range(1, 7):
        q.enq(i)
    print("Front:   ", q.front())
    print("Deq:     ", q.deq())
    q.print()
    print("Is empty?", q.is_empty())

def postfix_2_infix(q):
    s = Stack([])
    while not q.is_empty():
        c = q.deq()
        if c.isdigit():
            s.push(c)
        elif c in "+-/*":
            op2 = s.pop()
            op1 = s.pop()
            s.push("["+ op1 + c + op2 +"]")
    return s.pop()

print ('Q', end="")
print(postfix_2_infix(Queue( ['1','2','+'] )))
print ('Q', end="")
print(postfix_2_infix(Queue( ['5','4','*','7','+'] )))
print ('Q', end="")
print(postfix_2_infix(Queue( ['2','3','*','8','5','*','+'] )))