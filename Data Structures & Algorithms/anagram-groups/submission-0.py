class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = {}
        for index, word in enumerate(strs):
            sorted_word = ''.join(sorted(word))
            if sorted_word in sorted_dict:
                sorted_dict[sorted_word].append(word)
            else:
                sorted_dict[sorted_word] = [word]
        
        res = [sorted_dict[k] for k in sorted_dict]
        return res

        

