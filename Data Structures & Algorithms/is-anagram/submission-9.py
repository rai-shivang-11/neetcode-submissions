class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        hashA = [0]*26
        hashB = [0]*26
        for i in range(len(s)):
            hashA[ord(s[i])-ord('a')] +=1
            hashB[ord(t[i])-ord('a')] +=1
        for i in range(26):
            if hashA[i] != hashB[i]:
                return False
        return True