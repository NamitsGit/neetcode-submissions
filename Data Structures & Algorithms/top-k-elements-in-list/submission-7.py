class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_entries = k
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
            
        buckets = [[] for i in range(len(nums) + 1)]
       
        for key in counts:
            buckets[counts[key]].append(key)
        result = []

        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result


