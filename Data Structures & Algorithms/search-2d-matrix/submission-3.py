class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i_min, i_max = 0, len(matrix)
        i = 0
        while i_min <= i_max:
            i = (i_min + i_max) // 2
            if not ( i >= 0 and i < len(matrix)):
                i = -1
                break
            if target > matrix[i][-1]:
                i_min = i + 1
            elif target < matrix[i][0]:
                i_max = i - 1
            else:
                if matrix[i][0] <= target <= matrix[i][-1]:
                    break
                else:
                    i = -1
                    break
            
        
        if i == -1:
            return False
        
        l, r = 0, len(matrix[i])
        while l <= r:
            mid = (l + r) // 2
            if not (0 <= mid < len(matrix[i])):
                return False
            if target < matrix[i][mid]:
                r = mid - 1
            elif target > matrix[i][mid]:
                l = mid + 1
            else:
                return True
        
        return False
            



