class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for i in range(len(nums)):
            target = -nums[i]
            s = [nums[i]]
            r =i + 1
            l = len(nums) - 1
            while r < l:
                t = nums[r] + nums[l]
                if t == target:
                    s.append(nums[r])
                    s.append(nums[l])
                    #s.sort()
                    if len(s) !=1 and s not in out: 
                        out.append(s)
                    s = [nums[i]]
                    r += 1
                    l -= 1
                elif t > target:
                    l -=1
                else:
                    r +=1
        return out