class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        tot = row * col
        l, r = 0, tot - 1
        while l<=r:
            m = l + (r-l)//2
            ro = m // col
            co = m % col
            val = matrix[ro][co]
            if val == target: return True
            elif val < target: l = m+1
            else: r = m -1
        return False