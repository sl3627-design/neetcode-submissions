class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        d = {}
        s = 0
        for g in grid:
            for n in g:
                s += n
                if n in d:
                   repeated = n
                d[n] = 1

        n_squared = len(grid) ** 2
        tot = n_squared * (n_squared + 1) // 2

        missing = tot - (s - repeated)

        return [repeated, missing]


