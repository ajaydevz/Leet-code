class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ls = set()
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:]):
                if num1 == num2:
                    ls.add((i, j))
        return len(ls)


