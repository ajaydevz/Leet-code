class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
       nums = [i for i in nums if nums.count(i) == 1]
       return sum(nums)
       
       