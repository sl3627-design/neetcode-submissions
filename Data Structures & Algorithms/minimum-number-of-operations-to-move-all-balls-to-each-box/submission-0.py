class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        for i in range(len(boxes)):
            moves = 0
            for j in range(len(boxes)):
                if i == j:
                    continue
                else:
                    if boxes[j] == "1":
                        moves += abs(i-j)
                j += 1
            res.append(moves)
        
        return res