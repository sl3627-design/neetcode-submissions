class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        for i in range(len(mat)):
            res += mat[i][i]
        
        for i in range(len(mat)):
            mat[i] = mat[i][::-1]
        
        for i in range(len(mat)):
            res += mat[i][i]

        if len(mat) & 1:
            center = len(mat)//2
            res -= mat[center][center]

        
        return res