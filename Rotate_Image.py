https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            j=0
            k=len(matrix)-1
            while k>=j and i<=k:
                temp = matrix[i][k]
                matrix[i][k] = matrix[k][i]
                matrix[k][i] = temp
                #j+=1
                k-=1
                 
        for i in range(len(matrix)):
            j=0
            k=len(matrix)-1
            while j<k:
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][k]
                matrix[i][k] = temp
                j+=1
                k-=1
