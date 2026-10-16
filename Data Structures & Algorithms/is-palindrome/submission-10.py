class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = []
        for i in s:
            if not i.isspace() and i.isalnum():
                cleaned_s.append(i.lower())
        cleaned_s = ''.join(cleaned_s)
        if not cleaned_s:
            return True
        right = len(cleaned_s) - 1
        left = 0

        while left <= right and left <= len(cleaned_s) - 1 and right >= 0:
            if cleaned_s[right] != cleaned_s[left]:
                return False
            right -= 1
            left += 1
            
        return True