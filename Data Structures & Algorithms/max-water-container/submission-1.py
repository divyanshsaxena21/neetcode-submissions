class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l,r = 0,n-1
        max_area = 0
        while(l<r):
            h = min(heights[l],heights[r])
            # if (r-l)*h > max_area:
            max_area = max(max_area,(r-l)*h)
            if heights[r]<heights[l]:
                r-=1
            else:
                l+=1
        return max_area