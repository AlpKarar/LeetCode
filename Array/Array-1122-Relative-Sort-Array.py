class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        index_match = {arr2[i]: i for i in range(len(arr2))}
        freq_arr2 = [0] * len(arr2)
        other = []

        for num in arr1:
            if num in index_match:
                freq_arr2[index_match[num]] += 1
            else:
                other.append(num)
        
        res = []

        for j in range(len(arr2)):
            res += [arr2[j]] * freq_arr2[j]
        
        res += sorted(other)

        return res