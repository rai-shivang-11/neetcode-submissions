class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1

        if i < len(nums1):
            arr.extend(nums1[i:])
        else:
            arr.extend(nums2[j:])
        
        l = len(nums1) + len(nums2)

        if l%2==0:
            m1 = (l//2) - 1
            m2 = (l//2)
            return (arr[m1] + arr[m2])/2
        else:
            m = (l+1)//2
            m = m-1
            return arr[m]

        
    