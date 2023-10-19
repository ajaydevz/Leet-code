class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max1 = 0
        for i in accounts:
            sum1=0
            for k in i:
                sum1 = sum1+k
                if max1 < sum1:
                    max1 = sum1
        return max1

         
       
        