class Solution:
    def countBits(self, n: int) -> List[int]:
        out = []
        for i in range(n+1):
            bcount = 0
            while i:
                bcount += 1
                i = i & (i - 1)
            out.append(bcount)
        return out