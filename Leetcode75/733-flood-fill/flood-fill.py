class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dirs=[[0,1],[0,-1],[1,0],[-1,0]]
        m,n=len(image), len(image[0])
        start=image[sr][sc]
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n:
                return
            if image[i][j]!=start:
                return
            if image[i][j]==color:
                return
            image[i][j]=color
            for r,c in dirs:
                dr,dc=i+r,j+c
                dfs(dr,dc)
        dfs(sr,sc)
        return image