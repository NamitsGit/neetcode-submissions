class Solution:
    def isPalindrome(self, s: str) -> bool:
        no_space_str = s.lower().replace(' ', '')
        l, r = 0, len(no_space_str) - 1
        while l <= r:
            while l <= r and not no_space_str[l].isalnum():
                l += 1
            while l <= r and not no_space_str[r].isalnum():
                r -= 1
            if l <= r and no_space_str[l] != no_space_str[r]:
                return False
            l += 1
            r -= 1

        return True
        
