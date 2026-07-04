class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = dict(zip(heights, names))

        res = dict(sorted(d.items(), key = lambda item: item[0], reverse = True))

        return list(res.values())
