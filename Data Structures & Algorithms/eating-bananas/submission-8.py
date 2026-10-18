class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l = 1
        r = piles[-1]
        while l <=r:
            m = (l+r)//2
            hour = 0
            for p in piles:
                hour += math.ceil(p/m)
            if hour > h:
                l = m + 1
            else:
                r = m - 1
        
        return l