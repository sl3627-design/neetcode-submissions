class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct = {}; res = []
        for s in arr:
            if s not in distinct:
                distinct[s] = 1
            else:
                distinct[s] += 1
        for s in arr:
            if distinct[s] == 1:
                res.append(s)
        if len(res) < k:
            return ""
        return res[k-1]