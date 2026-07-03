class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            res.append([1]*(i+1))
        
        for row in range(numRows):
            for col in range(row + 1):
                if col == 0 or col == row:
                    res[row][col] = 1
                else:
                    res[row][col] = res[row-1][col-1] + res[row-1][col]
        
        return res
