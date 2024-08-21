class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedArr = sorted(nums1 + nums2)
        n = len(mergedArr)

        return (mergedArr[ n // 2] + mergedArr[n // 2 - 1]) / 2 if n % 2 == 0 else mergedArr[n // 2]