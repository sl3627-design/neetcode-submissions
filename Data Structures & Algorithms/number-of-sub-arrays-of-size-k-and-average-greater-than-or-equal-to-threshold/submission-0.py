class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s = sum(arr[:k])
        res = 0

        for i in range (k, len(arr)):
            if s >= k*threshold:
                res += 1
            s += arr[i] - arr[i-k]
        
        return res + (s >= k*threshold)