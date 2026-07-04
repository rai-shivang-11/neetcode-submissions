class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hMap = {']':'[', 
                '}':'{',
                ')':'(' }
        for b in s:
            if b in hMap:
                if stack and stack[-1] == hMap[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        
        if not stack: return True
        return False