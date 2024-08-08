# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: REVERSE QUEUE
#
# NAME:         John Kowal - Walter$
# ASSIGNMENT:   Project 2: Stacks & Queues

from Queue import Queue
from Stack import Stack

def flip(stack):
    f = Stack()  # Create a new stack
    while not stack.is_empty():
        f.push(stack.pop())
    return f

print('S', end="")
flip(Stack([1,2,3,4])).print()


# Return a new queue in reverse order
# Hint: can use a stack to help
def reverse(q_orig):
    q_new = Queue([])
    f = Stack()  # Create a new stack
    while not q_orig.is_empty():
        f.push(q_orig.deq())
    while not f.is_empty():
        q_new.enq(f.pop())

    return q_new

def main():
    q = Queue(list(range(1, 5)))
    q.print()
    print("reverse: ", end="")
    reverse(q).print()

# Don't run main on import
if __name__ == "__main__":
    main()
