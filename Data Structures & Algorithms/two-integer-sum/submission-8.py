class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffSet = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            diffSet[diff] = i

        for j in range(len(nums)):
            if nums[j] in diffSet and diffSet[nums[j]] !=j:
                return [min(diffSet[nums[j]],j),max(diffSet[nums[j]],j)]
        return [-1,-1]