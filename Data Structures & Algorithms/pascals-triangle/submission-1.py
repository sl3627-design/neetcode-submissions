class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # res = []
        # for i in range(numRows):
        #     res.append([1]*(i+1))
        
        # for row in range(numRows):
        #     for col in range(row + 1):
        #         if col == 0 or col == row:
        #             res[row][col] = 1
        #         else:
        #             res[row][col] = res[row-1][col-1] + res[row-1][col]
        
        # return res

        res = [[1]]

        for i in range (numRows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j+1])
            res.append(row)
        return res