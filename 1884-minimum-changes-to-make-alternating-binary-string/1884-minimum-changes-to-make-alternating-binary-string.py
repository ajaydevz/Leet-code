class Solution:
    def minOperations(self, s: str) -> int:
        count1 = 0
        count2 = 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == '1':
                    count1+= 1
                if s[i] == '0':
                    count2 += 1

            else:
                if s[i] == '0':
                    count1 += 1
                if s[i] == '1':
                    count2 += 1

        return min(count1,count2)