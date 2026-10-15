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
        seq_start_nums = set()
        for n in num_set:
            if n - 1 not in num_set and n + 1 in num_set:
                seq_start_nums.add(n)
        for n in seq_start_nums:
            print('within seq start nums : ', n)
            curr = n
            current_conseq = 1
            while curr + 1 in num_set:
                current_conseq += 1
                curr = curr + 1
            longest_conseq = max(longest_conseq, current_conseq)
        print(longest_conseq)
        return longest_conseq

        
        
        
        
