class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        dirs=[[1,0],[-1,0],[0,1],[0,-1]]
        m,n=len(isWater),len(isWater[0])
        res=[[0 for _ in range(n)] for _ in range(m)]
        visited=set()
        q=deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j]==1:
                    visited.add((i,j))
                    q.append((i,j))
        while q:
            i,j=q.popleft()
            for r,c in dirs:
                dr,dc=i+r,j+c
                if 0<=dr<m and 0<=dc<n and (dr,dc) not in visited and isWater[dr][dc]==0:
                    res[dr][dc]=res[i][j]+1
                    visited.add((dr,dc))
                    q.append((dr,dc))
        return res