class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabet_array = [0]*26
        for c1 in s:
            alphabet_array[ord(c1) - ord('a')] += 1
        
        for c2 in t:
            alphabet_array[ord(c2) - ord('a')] -= 1
        
        if alphabet_array != [0]*26:
            return False
        else:
            return True
