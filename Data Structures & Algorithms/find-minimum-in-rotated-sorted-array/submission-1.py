class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid = (l + r)//2
            res = min(res, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        





        
        
        
        
        
        
        # l, r = 0, len(nums) - 1
        # mid = (l + r)//2
        # res = nums[0]
        # while l <= r:
        #     if nums[l] < nums[r]:
        #         res = min(res, nums[l])
        #         break
        #     mid = (l+r)//2
        #     res = min(res, nums[mid])
        #     if nums[mid] >= nums[l]:
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        # return res
        