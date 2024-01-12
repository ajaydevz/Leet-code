class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        temp = '01'
        while temp in s:
            temp = '0' + temp + '1'
        return len(temp) -2