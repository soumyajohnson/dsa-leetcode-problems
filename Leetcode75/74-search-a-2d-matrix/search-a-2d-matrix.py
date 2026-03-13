class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=0
        m,n=len(matrix),len(matrix[0])
        l,h=0,n-1
        for i in range(m):
            if matrix[i][0]<=target<=matrix[i][n-1]:
                r=i
                break
        while l<=h:
            mid=(l+h)//2
            if matrix[r][mid]==target:
                return True
            elif matrix[r][mid]<target:
                l=mid+1
            else:
                h=mid-1
        return False