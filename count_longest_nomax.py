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
    current_l = 0
    previous_char = ""

    while not q.is_empty():
        char = q.deq()
        if char == previous_char:
            current_l += 1
        else:
            if current_l > max_l:
                max_l = current_l

            current_l = 1
            previous_char = char

    # Update max_l after the loop.
    if current_l > max_l:
        max_l = current_l
    return max_l

def main():
    print("out 2:", count_longest(Queue([l for l in "hello"])))
    print("out 5:", count_longest(Queue([l for l in "m" * 5])))
    print("out 3:", count_longest(Queue([l for l in "heee" ])))


# Don't run main on import
if __name__ == "__main__":
    main()

