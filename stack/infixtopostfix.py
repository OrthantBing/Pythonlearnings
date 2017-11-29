#Stack has pop and push access.
# User python lists, pop and append.
import re

class Stack:
    def __init__(self, list=None):
        if list is None:
            self.array = []
            self.count = 0
        else:
            self.array = list
            self.count = len(list)

    def push(self, string):
        self.array.append(string)
        self.count += 1

    def pop(self):
        self.count -= 1
        return self.array.pop()

    def peek(self):
        return self.array[self.count - 1]

    def isEmpty(self):
        if self.count == 0:
            return True
        return False

def infixToPostfix(infixexpr):
    priorityhash = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1
    }

    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        print opStack.array
        print postfixList
        if re.match(r'[a-zA-Z0-9]', token) is not None:
            postfixList.append(token)

        elif token == '(':
            opStack.push(token)

        elif token == ')':
            topToken = opStack.pop()
            while topToken is not '(':
                postfixList.append(topToken)
                topToken = opStack.pop()

        else:
            while (not opStack.isEmpty()) and (priorityhash[opStack.peek()] >= priorityhash[token]):
                postfixList.append(opStack.pop())

            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return " ".join(postfixList)

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
