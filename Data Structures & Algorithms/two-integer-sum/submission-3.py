class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums = {}
        for i, n in enumerate(nums):
            target_diff = target - n
            if target_diff in seen_nums:
                if i < seen_nums[target_diff]:
                    return [i, seen_nums[target_diff]]
                else:
                    return [seen_nums[target_diff], i]
            else:
                seen_nums[n] = i