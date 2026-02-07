class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs=[[0,1],[1,0],[0,-1],[-1,0]]
        rows,cols=len(grid),len(grid[0])
        fresh=0
        q=deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    q.append((i,j))
        mins=0
        while q and fresh>0:
            for _ in range(len(q)):
                row,col=q.popleft()
                for dr, dc in dirs:
                    r,c=row+dr,col+dc
                    if 0<=r<rows and 0<=c<cols and grid[r][c]==1:
                        grid[r][c]=2
                        fresh-=1
                        q.append((r,c))
            mins+=1
        return mins if fresh==0 else -1