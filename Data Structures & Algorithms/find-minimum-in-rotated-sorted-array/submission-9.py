class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if len(nums) == 1: return nums[0]
        while l < r:
            m = l + (r-l)//2
            if r - l <= 1: return min(nums[r],nums[l])
            if nums[l] > nums[m]:
                r = m
            elif nums[r] < nums[m]:
                l = m
            else:
                return nums[0]
        
        return nums[m]