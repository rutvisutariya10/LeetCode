            if token in "+-*/":
                op2 = stack.pop()
                op1 = stack.pop()
                if token == '+':
                    op1 += op2
                elif token == '-':
                    op1 -= op2
                elif token == '*':
                    op1 *= op2
                else:
                    op1 = trunc(op1/op2)
                stack.append(op1)
            else:
        for token in tokens:
        ans = 0
        stack = []
    def evalRPN(self, tokens: List[str]) -> int:
                stack.append(int(token))
