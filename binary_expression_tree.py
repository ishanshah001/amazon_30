class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def expTree(self, s: str) -> 'Node':
        def build():
            op = ops.pop()
            right = nodes.pop()
            left = nodes.pop()
            nodes.append(Node(op, left, right))

        prec = {'+': 1, '-': 1, '*': 2, '/': 2}
        nodes, ops = [], []

        for c in s:
            if c.isdigit():  # Operand → push to nodes stack
                nodes.append(Node(c))
            elif c in prec:  # Operator → resolve higher/equal precedence first. Atleast one operator should be in.
                while ops and ops[-1] in prec and prec[ops[-1]] >= prec[c]:
                    build()
                ops.append(c)
            elif c == '(':
                ops.append(c)
            elif c == ')':   # Resolve until '('
                while ops[-1] != '(':
                    build()
                ops.pop()  # Remove '('

        # Build remaining operations
        while ops:
            build()

        return nodes[-1]
