class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for rows in matrix:
            rows.reverse()
        for i in range(n):
            for j in range(n):
                if i+j<n-1:
                    matrix[i][j],matrix[n-j-1][n-i-1]=matrix[n-j-1][n-i-1],matrix[i][j]