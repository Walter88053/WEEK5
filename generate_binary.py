# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 3: GENERATE BINARY NUMBER STRINGS
#
# NAME:         John Kowal - Walter$
# ASSIGNMENT:   Project 2: Stacks & Queues

from Queue import Queue

def generate_binary_numbers(N):
    # FIXME
    returnq = Queue()
    if N <= 0:
        return returnq

    tempq = Queue()
    tempq.enq("1")

    for i in range(N):
        X = tempq.deq()
        returnq.enq(X)
        tempq.enq(X + "0")
        tempq.enq(X + "1")
    return returnq

def main():
    generate_binary_numbers(2).print()
    generate_binary_numbers(3).print()
    generate_binary_numbers(6).print()


# Don't run main on import
if __name__ == "__main__":
    main()

