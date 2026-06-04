class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = 0 
        l = len(numbers) - 1
        while r < l:
            t = numbers[r] + numbers[l]
            if t == target:
                return [r+1,l+1]
            elif t > target:
                l -=1
            else:
                r +=1
        
        return -1