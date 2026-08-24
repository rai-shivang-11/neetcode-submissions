class Solution:
    def hammingWeight(self, n: int) -> int:
        # Unsigned bit is binary representation
        # So if n = 100, actual number is 4x1 + 2x0 + 1x0 = 4
        
        # ----- Solution 1 -----
        # We can do a n%2 to see if the right most bit is 1 or 0
        # For odd numbers rightmost bit is 1, and 0 for even
        # To shift the bit representation to the right we can do n/2
        # This will change n = 100 to n = 10
        # 100/2 = 4x1 + 2x0 + 1x0/2 (Decimal) = 2x1 + 1x0 (decimal)= 10 (binary)
        # res = 0
        # while n:
        #     res = n%2           # Tells if the rightmost bit is a 1 or a 0 
        #     #n = n // 2         # Shifts the binary representaion to the right (// to keep n as an integer)
        #     n = n >> 1          # Bitwise operator to shift bits to the right by 1
        # return res

        # ----- Solution 2 -----
        # Weird but brilliant, to avoid looping unncessarily over all the 0s
        # We do n & (n - 1)
        # Refer to the video for more detail
        # But it works becuase n - 1 changes the first 1 to 0 from right
        # The & is used to eliminate any 1 that was introduced as a result of the subtraction
        res = 0
        while n:
            res += 1
            n = n & (n - 1)
        return res
