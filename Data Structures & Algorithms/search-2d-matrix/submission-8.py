class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        r = (rows * cols) - 1
        l = 0
        while l <= r:
            m = (l+r)//2
            row = m // cols
            col = (m % cols)
            val = matrix[row][col]
            if target == val: return True
            elif val > target: r = m - 1
            else: l = m +1
        return False 