class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        res = ""

        for i in range(len(order)):
            if order[i] in count:
                res += order[i]*count[order[i]]
                del count[order[i]]
        
        for key, value in count.items():
            res += key*value
    
        return res