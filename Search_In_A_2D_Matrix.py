https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = m * n - 1
        while(i <= j):
            mid = (i + (j-i)//2)
            if matrix[mid//n][mid % n] == target:
                return True
            if matrix[mid//n][mid % n] < target:
                i = mid + 1
            else:
                j = mid - 1
        return False