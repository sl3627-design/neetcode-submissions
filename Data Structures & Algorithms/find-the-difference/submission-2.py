class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = Counter(s)
        count_t = Counter(t)
        for ss in s:
            if ss in count_t and count_t[ss] == 1:
                del count_t[ss]
            else:
                count_t[ss] -= 1
        
        return "".join(list(count_t.keys()))