class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        pro = 1
        c = 0
        iZero =-1
        for i,n in enumerate(nums):
            if n == 0:
                c+=1
                if c > 1:
                    pro = 0
                iZero = i
                continue
            else:
                pro = pro * n
            
        if pro == 0:
            out = [0] * len(nums)
            return out
        out = []
        for k,j in enumerate(nums):
            if iZero != -1:
                if k == iZero:
                    out.append(pro)
                else:
                    out.append(0)
            else:
                out.append(pro//j)
        return out