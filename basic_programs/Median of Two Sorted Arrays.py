class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        k = 0
        final = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                final.append(nums1[i])
                i = i + 1
            else:
                final.append(nums2[j])
                k = k + 1
                j = j + 1
        if i < len(nums1):
            final = final + nums1[i:len(nums1)]
        
        if j < len(nums2):
            final = final + nums2[j:len(nums2)]
        if len(final)%2 == 0:
            return (final[len(final)//2 - 1] + final[len(final)//2]) / 2
        else:
            return final[len(final)//2]
