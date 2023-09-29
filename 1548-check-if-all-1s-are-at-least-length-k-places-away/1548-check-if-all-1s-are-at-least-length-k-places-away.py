class Solution(object):
    def kLengthApart(self, nums, k):
        n = k
        for i in nums:
            if i == 0:
                n += 1
            else:
                if n < k :
                    return False
                n = 0
        return True
        
        