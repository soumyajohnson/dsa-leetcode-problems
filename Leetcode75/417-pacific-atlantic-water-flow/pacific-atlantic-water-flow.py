class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs=[[1,0],[-1,0],[0,1],[0,-1]]
        pac=set()
        atl=set()
        m,n=len(heights),len(heights[0])
        # for i in range(m):
        #     for j in range(n):
        #         if i==0 or j==0:
        #             pac.append([i,j])
        #         if i==m-1 or j==n-1:
        #             atl.append([i,j])
        def dfs(i,j,visited):
            if i<0 or i>=m or j<0 or j>=n or (i,j) in visited:
                return 
            visited.add((i,j))
            for r,c in dirs:
                dr,dc=i+r,j+c
                if 0<=dr<m and 0<=dc<n and (dr,dc) not in visited and heights[dr][dc]>=heights[i][j]:
                    dfs(dr,dc,visited)
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    dfs(i,j,pac)
                if i==m-1 or j==n-1:
                    dfs(i,j,atl)
        res=[]
        for i in range(m):
            for j in range(n):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        return res
