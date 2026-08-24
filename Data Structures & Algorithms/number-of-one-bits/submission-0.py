class Solution:
    def hammingWeight(self, n: int) -> int:
        # Unsigned bit is binary representation
        # So if n = 100, actual number is 4x1 + 2x0 + 1x0 = 4
        # We can do a n%2 to see if the right most bit is 1 or 0
        # For odd numbers rightmost bit is 1, and 0 for even
        # To shift the bit representation to the right we can do n/2
        # This will change n = 100 to n = 10
        # 100/2 = 4x1 + 2x0 + 1x0/2 (Decimal) = 2x1 + 1x0 (decimal)= 10 (binary)
        res = 0
        while n:
            if n%2:             # Tells if the rightmost bit is a 1 or a 0 
                res +=1
            n = n // 2          # Shifts the binary representaion to the right
        return res