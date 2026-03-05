class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n=len(board),len(board[0])
        dirs=[[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(i,j):
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]!='O':
                return
            board[i][j]='T'
            for dr,dc in dirs:
                dfs(i+dr,j+dc)
        for i in range(m):
            if board[i][0]=='O':
                dfs(i,0)
            if board[i][n-1]=='O':
                dfs(i,n-1)
        for j in range(n):
            if board[0][j]=='O':
                dfs(0,j)
            if board[m-1][j]=='O':
                dfs(m-1,j)
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j]='X'
                if board[i][j]=='T':
                    board[i][j]='O'
