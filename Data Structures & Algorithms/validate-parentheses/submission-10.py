class Solution:
    def isValid(self, s: str) -> bool:
        b_open = "({["
        b_key = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        b_stack = []
        for b in s:
            if b in b_open:
                b_stack.append(b)
            else:
                if len(b_stack) == 0:
                    return False

                b_valid = b_key[b]
                b_close = b_stack.pop()
                if b_close != b_valid:
                    return False

        if len(b_stack) != 0: return False 
        return True
