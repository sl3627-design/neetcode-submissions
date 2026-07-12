class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        while len(stones) > 1:
            stones.sort()
            temp = stones[len(stones) - 1] - stones[len(stones) - 2]
            stones.pop()
            stones.pop()
            stones.append(temp)
        
        return stones[0]