class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum1 = 0
        sum2 = 0
        for i in range(1,n+1):
            if i % m != 0:
                sum1 += i
            else:
                sum2+= i
        return sum1 - sum2

