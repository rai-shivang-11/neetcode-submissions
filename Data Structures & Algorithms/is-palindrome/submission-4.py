class Solution:
    import re
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        strin = re.sub(r'[^a-zA-Z0-9]', '', s)
        r = 0
        l = len(strin) -1
        while r < l:
            if strin[r] !=  strin[l]: return False
            r+=1
            l-=1
        return True