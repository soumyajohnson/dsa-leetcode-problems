class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea=0
        l,r=0,len(height)-1
        while l<=r:
            area=(r-l)*min(height[l],height[r])
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
            maxarea=max(maxarea,area)
        return maxarea


        