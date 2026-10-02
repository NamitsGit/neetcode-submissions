class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in d:
                if d[diff] < i:
                    return [d[diff], i]
                else:
                    return [i, d[diff]]
            else:
                d[n] = i
        return []