class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        container_max_area = 0
        while i < j:
            area = (j - i) * min(heights[j], heights[i])
            container_max_area = max(area, container_max_area)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return container_max_area

        