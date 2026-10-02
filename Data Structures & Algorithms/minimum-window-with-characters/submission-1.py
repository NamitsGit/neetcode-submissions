class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" : return ""
        substr_count, target_count = {}, {}
        res = [-1, -1]
        res_len = float("infinity")
        l = 0
        for c in t: target_count[c] = 1 + target_count.get(c, 0)
        have, need = 0, len(target_count)
        for r in range(len(s)):
            c = s[r]
            substr_count[c] = 1 + substr_count.get(c, 0)

            if c in target_count and substr_count[c] == target_count[c]:
                have += 1
            
            while need == have:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = (r - l + 1)
                
                substr_count[s[l]] -= 1
                
                if s[l] in target_count and substr_count[s[l]] < target_count[s[l]]:
                    have -= 1
                    
                l += 1
        
        l, r = res
        return s[l : r + 1] if res_len != float("infinity") else ""


        # if t == "": return ""

        # target_count = {}
        # substr_count = {}
        # for c in t: target_count[c] = 1 + target_count.get(c, 0)
        # have, need = 0, len(target_count.keys())
        # res = [-1, -1]
        # res_len = float("infinity")

        # l = 0
        # for r in range(len(s)):
        #     c = s[r]
        #     substr_count[c] = 1 + substr_count.get(c, 0)

        #     if c in target_count and substr_count[c] == target_count[c]:
        #         have += 1

        #     while have == need:
        #         if (r - l + 1) < res_len:
        #             res = [l, r]
        #             res_len = (r - l + 1)
        #         substr_count[s[l]] -= 1
        #         if s[l] in target_count and substr_count[s[l]] < target_count[s[l]]:
        #             have -= 1
                
        #         l += 1
                

        # l, r = res
        # return s[l:r+1] if res_len != float("infinity") else ""
                
