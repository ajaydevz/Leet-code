class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        num_count = Counter(nums)
        for count in num_count.values():
            if count > 2 :
                return False
        return True