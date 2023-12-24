class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}
        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_index:
                return [num_index[complement], i]

            num_index[num] = i
        return -1
    