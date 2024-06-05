class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count_dict_list = []
        min_i = 0
        min_len = 100

        for i in range(len(words)):
            count_dict = dict()

            for letter in words[i]:
                count_dict[letter] = count_dict.get(letter, 0) + 1
            
            count_dict_list.append(count_dict)
            
            if len(count_dict) < min_len:
                min_len = len(count_dict)
                min_i = i

        res = []

        for letter in count_dict_list[min_i]:
            min_count = count_dict_list[min_i][letter]
            isPresent = True

            for j in range(len(count_dict_list)):
                if letter not in count_dict_list[j]:
                    isPresent = False
                    break
                
                if j != min_i:
                    min_count = min(min_count, count_dict_list[j][letter])
            
            if isPresent:
                res += [letter] * min_count
        
        return res