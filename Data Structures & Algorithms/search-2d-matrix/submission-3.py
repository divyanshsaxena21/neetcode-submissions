class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = 0
        n = len(matrix)
        m = len(matrix[0])
        while(r<n):

            if matrix[r][m-1]<target:
                r+=1
            elif target>=matrix[r][0] and target<=matrix[r][m-1]:
                low,high = 0,m
                while(low<=high):
                    mid = low + (high-low)//2
                    if matrix[r][mid] == target:
                        return True
                    elif matrix[r][mid]>target:
                        high = mid - 1
                    else:
                        low = mid + 1
                r+=1
            else:
                r += 1
        return False
