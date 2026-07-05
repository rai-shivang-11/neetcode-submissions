class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []
        for s in tokens:
            if s in operators:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if s == '+': o = num1 + num2
                if s == '-': o = num1 - num2
                if s == '*': o = num1 * num2
                if s == '/': o = int(num1/num2)
                stack.append(o)
            else:
                stack.append(s)
        return int(stack.pop())