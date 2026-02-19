class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n=len(board), len(board[0])
        live=0
        dirs=[(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]
        for i in range(m):
            for j in range(n):
                live=0
                for dr,dc in dirs:
                    if 0<=i+dr<m and 0<=j+dc<n and abs(board[i+dr][j+dc])==1:
                        live+=1
                if board[i][j]==1:
                    if live<2 or live >3:
                        board[i][j]=-1
                else:
                    if live==3:
                        board[i][j]=2

        for i in range(m):
            for j in range(n):
                board[i][j]=1 if board[i][j]>0 else 0