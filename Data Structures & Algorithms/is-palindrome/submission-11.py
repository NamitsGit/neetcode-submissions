class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not is_alpha_num(s[left]):
                left += 1
            while right > left and not is_alpha_num(s[right]):
                right -= 1
        
            if s[right].lower() != s[left].lower():
                return False
            
            right -= 1
            left += 1

        return True
    
def is_alpha_num(char:str)->bool:
    return (
        ord('A') <= ord(char) <= ord('Z') or
        ord('a') <= ord(char) <= ord('z') or
        ord('0') <= ord(char) <= ord('9')
        )