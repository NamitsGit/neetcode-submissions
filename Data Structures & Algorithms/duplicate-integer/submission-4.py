class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result_dict = {}
        for n in nums:
            if n in result_dict:
                return True
            else:
                result_dict[n] = 1
        return False