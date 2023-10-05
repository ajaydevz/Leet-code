class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [x for x in set(nums) if nums.count(x)>len(nums)/3]
        



        