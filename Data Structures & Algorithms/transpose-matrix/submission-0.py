class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        mat = matrix
        res = [[[0] for _ in range(len(mat))] for _ in range(len(mat[0]))]
        for i in range (len(res)):
            for j in range (len(res[0])):
                res[i][j] = mat[j][i]
        
        return res