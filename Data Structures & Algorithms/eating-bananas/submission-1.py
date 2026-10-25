class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 1
        max_rate = max(piles)
        l, r = 1, max_rate
        res = max_rate
        while l <= r:
            k = (l + r) // 2
            hours = self.hoursToFinish(piles, k)
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res
            
           
            
    def hoursToFinish(self, piles, k):
        hours = 0
        for pile in piles:
            if pile < k:
                hours += 1
            else:
                hours += math.ceil(pile/k)
        
        return hours