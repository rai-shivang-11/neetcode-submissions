class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, r1 = 0, len(nums1)-1
        l2, r2 = 0, len(nums2)-1
        comb = [0] * (len(nums1) + len(nums2))
        l = 0
        while True:
            if l1 > r1:
                comb[l:] = nums2[l2:]
                break
            if l2 > r2:
                comb[l:] = nums1[l1:]
                break
            if nums1[l1] < nums2[l2]:
                comb[l] = nums1[l1]
                l1 += 1
            else:
                comb[l] = nums2[l2]
                l2 += 1
            l+=1
        n = len(comb)
        if n%2 == 0:
            m1 = n//2
            m2 = m1-1
            return (comb[m2] + comb[m1]) / 2
        else:
            m = n//2
            return comb[m]