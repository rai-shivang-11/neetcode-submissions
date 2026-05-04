class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dMap = {}
        def word(i,w):
            if (i,w) in dMap:
                return dMap[(i,w)]
            if w == t:
                dMap[(i,w)] = 1
                return 1
            elif (i >= len(s)) or (len(w) > len(t)):
                dMap[(i,w)] = 0
                return 0 
            else:
                dMap[(i,w)] = word(i+1,w+s[i]) + word(i+1,w)
                return dMap[(i,w)]
        out = word(0,"")
        return out

        