class Solution(object):
    def sortArrayByParity(self, nums):
        a = []
        for i in nums:
            if i % 2 == 0:
                a.insert(0,i)
            else:
                a.append(i)
        return a

        