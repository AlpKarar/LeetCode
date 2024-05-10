class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        name_height = [(names[i], heights[i]) for i in range(len(names))]
        sorted_name_height = sorted(name_height, key = lambda x: x[1])[::-1]

        return [item[0] for item in sorted_name_height]