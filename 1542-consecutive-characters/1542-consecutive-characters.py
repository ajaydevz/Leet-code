class Solution(object):
    def maxPower(self, s):
        max_count = 1 
        current_count = 1

        for i in range(1, len(s)):  
            if s[i] == s[i-1]:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 1

        return max_count







