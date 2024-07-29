class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp_nums1 = nums1[:m]
        idx = 0
        i = 0
        j = 0

        while i < m and j < n:
            if temp_nums1[i] < nums2[j]:
                nums1[idx] = temp_nums1[i]
                i += 1
            else:
                nums1[idx] = nums2[j]
                j += 1

            idx += 1
        
        while i < m:
            nums1[idx] = temp_nums1[i]
            i += 1
            idx += 1
        
        while j < n:
            nums1[idx] = nums2[j]
            j += 1
            idx += 1