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

        # Why returning l works?
        # Assume we stumble on the answer at somepoint
        # At that point our algo will set r = m -1, just short of the answer
        # Now after that we'll not find any m that satisfies the condition
        # So in that case our l will keep on increasing
        # At some point l = r = m and we will still not get a match
        # Then as a final update l = m + 1, which is r + 1, our required answer