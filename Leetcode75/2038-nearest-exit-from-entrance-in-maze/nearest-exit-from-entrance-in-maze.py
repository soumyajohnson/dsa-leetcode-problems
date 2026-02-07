class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        dirs=[[0,1],[1,0],[0,-1],[-1,0]]
        rows=len(maze)
        cols=len(maze[0])
        x0,y0=entrance[0], entrance[1]
        q=deque([(x0,y0,0)])
        maze[x0][y0]='+'
        while q:
            x,y,s=q.popleft()
            for dr,dc in dirs:
                x1,y1=x+dr,y+dc
                if 0<=x1<rows and 0<=y1<cols and maze[x1][y1]=='.':
                    if x1==0 or x1==rows-1 or y1==0 or y1==cols-1:
                        return s+1
                    maze[x1][y1]='+'
                    q.append((x1,y1,s+1))
        return -1