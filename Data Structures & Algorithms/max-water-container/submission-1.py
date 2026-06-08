class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r = 0
        l = len(heights)-1
        mArea = -1
        while r < l:
            area = min(heights[r],heights[l]) * (l-r)
            if area > mArea: mArea = area

            if heights[r] < heights[l]: r+=1
            else: l-=1
        return mArea
