class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dirs=[[1,0],[-1,0],[0,1],[0,-1]]
        q=deque()
        visited=set()
        m,n=len(mat),len(mat[0])
        res=[[ 0 for _ in range (n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    visited.add((i,j))
                    q.append((i,j))
        while q:
            for _ in range(len(q)):
                i,j=q.popleft()
                for r,c in dirs:
                    dr,dc=r+i,j+c
                    if 0<=dr<m and 0<=dc<n and (dr,dc) not in visited and mat[dr][dc]==1:
                        res[dr][dc]=res[i][j]+1
                        visited.add((dr,dc))
                        q.append((dr,dc))
        return res
