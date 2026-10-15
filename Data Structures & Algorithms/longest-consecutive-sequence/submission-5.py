class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        longest_conseq = 1
        current_conseq = 1

        # brute force 
        # for n in nums:
        #     curr_seq = n
        #     prev_num = n
        #     current_conseq = 1
        #     while curr_seq + 1 in num_set:
        #         prev_num = curr_seq
        #         curr_seq += 1
        #         current_conseq += 1
        #     longest_conseq = max(longest_conseq, current_conseq)
        # return longest_conseq

        # finding the sequence start numbers
        for n in nums:
            if (n - 1) not in num_set:
                length = 0
                while n + length in num_set:
                    length += 1
                longest_conseq = max(longest_conseq, length)

        return longest_conseq

        
        
        
        
