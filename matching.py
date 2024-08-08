# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: BRACE MATCHER
#
# NAME:         John Kowal - Walter$
# ASSIGNMENT:   Project 2: Stacks & Queues

from Stack import Stack

# Returns True if the braces match,
# & False otherwise
def matcher(str):
    s = Stack([])
    # FIXME

    opening_brackets = "([{"
    closing_brackets = ")]}"
    match = {'(': ')', '[': ']', '{': '}'}

    for char in str:
        if char in opening_brackets:
            s.push(char)
        elif char in closing_brackets:
            if s.is_empty() or match[s.peek()] != char:
                return False
            s.pop()
    return s.is_empty()
    return True

print(matcher("[()]"))
print(matcher("[("))
print(matcher("hello"))




def main():
    print("matcher: ", matcher("[()]"))

# Don't run main on import
if __name__ == "__main__":
    main()

