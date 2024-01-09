class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        res = []
        l1 = []
        l2 = []
        l3 = []
        l1 = [1]*numOnes
        l2 = [0]*numZeros
        l3 = [-1]*numNegOnes
        res = l1+l2+l3
        return sum(res[:k])


        
