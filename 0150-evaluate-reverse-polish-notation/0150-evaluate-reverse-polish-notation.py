class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for t in tokens:
            if t in "+-*/":
                op2 = stack.pop()
                op1 = stack.pop()
                if t == '+':
                    res = op1 + op2
                elif t == '-':
                    res = op1 - op2
                elif t == '*':
                    res = op1 * op2
                elif t == '/':
                    res = op1 / op2
                stack.append(int(res))
            else:
                stack.append(int(t))
        return stack[0]
    

    def evalRPN2(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok in "+-*/":
                op2 = stack.pop()
                op1 = stack.pop()
                if tok == "+":
                    stack.append(op1 + op2)                
                elif tok == "-":
                    stack.append(op1 - op2)                
                elif tok == "*":
                    stack.append(op1 * op2)                
                else:
                    stack.append(int(op1 / op2))
            else:
                stack.append(int(tok))
        return stack[0]