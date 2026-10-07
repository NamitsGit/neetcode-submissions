class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_entries = k
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
        # print(f"{counts=}")
        buckets = []
        for i in range(len(nums)+1):
            buckets.append([])
        # print(f"{buckets=}")
        for key in counts:
            # print(f"{key=} {counts[key]=}")
            buckets[counts[key]].append(key)
            # print(f"UPDATED BUCKET : {buckets=}")
        # print(f"filled buckets {buckets=}")
        result = []

        for freq in range(len(nums), 0, -1):
            if buckets[freq] == []:
                continue
            # print(f"non empty bucket {buckets[freq]=}")
            if k == 0:
                break
            result.extend(buckets[freq])
            k -= 1
            # print(f" k > 0 {k=} {result=}")

        return result[:num_entries]

