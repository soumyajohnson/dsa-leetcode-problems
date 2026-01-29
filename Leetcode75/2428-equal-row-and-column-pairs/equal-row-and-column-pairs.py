class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n=len(grid)
        rowcount=defaultdict(int)
        for row in grid:
            rowcount[tuple(row)]+=1
        count=0
        for c in range(n):
            col=[]
            for r in range(n):
                col.append(grid[r][c])
            colval=tuple(col)
            count+=rowcount[colval]

        return count