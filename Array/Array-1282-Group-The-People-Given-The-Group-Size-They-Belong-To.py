class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = dict()

        for i in range(len(groupSizes)):
            if groupSizes[i] in groups:
                groups[groupSizes[i]].append(i)
            else:
                groups[groupSizes[i]] = [i]
        
        res = []

        for group in groups:
            if len(groups[group]) > group:
                s = 0
                e = group

                while e <= len(groups[group]):
                    res.append(groups[group][s:e])
                    s = e
                    e += group
            else:
                res.append(groups[group])
        
        return res