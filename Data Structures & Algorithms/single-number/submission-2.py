class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # We'll use bit manipulation
        # Particularly XOR: ^ (operator)
        # XOR returns 1 if the two imputs are different and 0 if they're the same
        # So if we take each element of the list and do an XOR
        # we'll end up with a number that doesn't repeat
        # Note: n ^ 0 = n (1 ^ 0 = 1 and 0 ^ 0 = 0) so this is always true

        res = 0
        for n in nums:
            res = res ^ n
        
        return res