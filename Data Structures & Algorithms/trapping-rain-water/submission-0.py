class Solution:
    def trap(self, height: List[int]) -> int:
        #right pass
        r = 0
        prev = 0
        rWater = [0]*len(height)
        while r < len(height):
            val = prev - height[r]
            if val >=0: rWater[r] = val
            else: rWater[r] = 0
            prev = max(prev,height[r])
            r+=1
        #left pass
        l = len(height)-1
        prev = 0
        lWater = [0]*len(height)
        out = 0
        while l >= 0:
            val = prev - height[l]
            if val >=0: lWater[l] = val
            else: lWater[l] = 0
            out += min(lWater[l],rWater[l])
            prev = max(prev,height[l])
            l-=1

        return out