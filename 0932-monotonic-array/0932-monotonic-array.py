class Solution(object):
    def isMonotonic(self, nums):
	return nums == sorted(nums) or nums == sorted(nums, reverse=True)
        
        