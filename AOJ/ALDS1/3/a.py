src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/3/ALDS1_3_A"

# ---- solution ----


class Stack:
    def __init__(self):
        """
        initialize stack.
        """
        self.data = []
        self.pos = 0

    def push(self, x):
        """
        push an element into stack.
        """
        self.data.append(x)
        self.pos += 1

    def pop(self):
        """
        pops an element out of stack.
        """
        if self.pos == 0:
            return IndexError("Stack is empty!")
        else:
            self.pos -= 1
            return self.data.pop()


def rpn(*args):
    """
    docstring
    """
    o1, o2 = int(args[0]), int(args[1])
    if args[2] == "+":
        return o1 + o2
    elif args[2] == "-":
        return o2 - o1
    elif args[2] == "*":
        return o1 * o2


operators = "+-*"

# ---- process ----


stack = input().split()
s = Stack()
for i in stack:
    if i not in operators:
        s.push(int(i))
    else:
        o1 = s.pop()
        o2 = s.pop()
        s.push(rpn(o1, o2, i))
print(s.pop())
