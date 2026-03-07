class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n=len(board)
        def get_pos(num):
            r=(num-1)//n
            c=(num-1)%n
            row=n-r-1
            if r%2==1:
                c=n-c-1
            return row,c
        q=deque([(1,0)])
        visited=set([1])
        while q:
            num,moves=q.popleft()
            if n*n==num:
                return moves
            for i in range(1,7):
                next_num=num+i
                if next_num>n*n:
                    continue
                r,c=get_pos(next_num)
                if board[r][c]!=-1:
                    next_num=board[r][c]
                if next_num not in visited:
                    visited.add(next_num)
                    q.append((next_num, moves+1))
        return -1
