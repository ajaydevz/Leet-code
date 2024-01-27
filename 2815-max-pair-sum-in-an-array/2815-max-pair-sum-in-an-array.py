class Solution:
    def maxSum(self, nums: List[int]) -> int:
        maxi=-1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                m=max(str((nums[i])))
                n=max(str(str(nums[j])))
                if m==n:
                    c=nums[i]+nums[j]
                    maxi=max(maxi,c)
        return maxi