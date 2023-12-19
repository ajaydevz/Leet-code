class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        num_set=set(nums)
        max_k = -1

        for i in nums:
            if -i in nums:
                max_k = max(max_k,abs(i))
        
        return max_k
            
                

        