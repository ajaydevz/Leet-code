class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sum = 0
        for i in range(len(str(n))):
            if i % 2 == 0:
                sum += int(str(n)[i])
            else:
                sum += -int(str(n)[i])
        return sum

        