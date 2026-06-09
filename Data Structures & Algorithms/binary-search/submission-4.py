# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         l, r = 0, len(nums)
#         while l <= r:
#             m = l + ((r - l) // 2)
#             if nums[m] == target: return m
#             elif target > nums[m]: l = m + 1
#             else: r = m - 1
#         return -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            # (l + r) // 2 can lead to overflow
            m = l + ((r - l) // 2)

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1