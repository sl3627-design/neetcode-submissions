class Solution:
    def maxScore(self, s: str) -> int:
        # Count total ones in the string
        ones_count = s.count('1')
        
        zeros_left = 0
        ones_right = ones_count
        max_score = 0
        
        # Iterate through valid split points (leaving at least 1 char for the right side)
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros_left += 1
            else:
                ones_right -= 1
                
            current_score = zeros_left + ones_right
            if current_score > max_score:
                max_score = current_score
                
        return max_score
                      