class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        out = r + 1
        while l <=r:
            m = l + (r-l)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/m)
            if hours > h:
                l = m +1
            else:
                r = m - 1
                out = min(out, m)
        return out