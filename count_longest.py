# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 4: COUNT THE LONGEST SUBSEQUENCE
#
# NAME:         John Kowal - Walter$
# ASSIGNMENT:   Project 2: Stacks & Queues

from Queue import Queue

# count longest sequence of duplicates in a queue
# can destroy the queue & make it empty
def count_longest(q):
    # FIXME
    if q.is_empty():
        return 0
    max_l = 0
    current_l = 1
    last = q.deq()
    while not q.is_empty():
        current = q.deq()
        if current == last:
            current_l += 1
        else:
            max_l = max(max_l, current_l)
            current_l = 1
            last = current
    max_l = max(max_l, current_l)
    return max_l

def main():
    print("out 2:", count_longest(Queue([l for l in "hello"])))
    print("out 5:", count_longest(Queue([l for l in "m" * 5])))
    print("out 3:", count_longest(Queue([l for l in "heee"])))


# Don't run main on import
if __name__ == "__main__":
    main()

