class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        result = list(set(nums))
        result.sort(reverse=True)
        if len (result) >= 3:
            return result[2]
        return max(result)


        

        