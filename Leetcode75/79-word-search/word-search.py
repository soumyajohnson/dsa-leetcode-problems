class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen=set()
        m,n=len(board),len(board[0])
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(i,j,k):
            if not (0<=i<m and 0<=j<n):
                return False
            if board[i][j]!=word[k]:
                return False
            if k==len(word)-1:
                return True
            seen.add((i,j))
            for dr,dc in dirs:
                di,dj=dr+i,dc+j
                if (di,dj) not in seen:
                    if dfs(di,dj,k+1):
                        return True
            seen.remove((i,j))
            return False
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False