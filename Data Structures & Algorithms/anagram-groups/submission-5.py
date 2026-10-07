class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            chr_arr = [0] * 26
            for c in s:
                chr_arr[ord(c) - ord('a')] += 1
            res[tuple(chr_arr)].append(s)
        return list(res.values())