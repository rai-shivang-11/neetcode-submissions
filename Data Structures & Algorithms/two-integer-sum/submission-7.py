class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSet = {}
        for i,n in enumerate(nums):
            if n in hashSet.keys():
                return [hashSet[n], i]
            hashSet[target - n] = i
        return

        