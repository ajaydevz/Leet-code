class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        output=[]
        for i in range(0,len(nums),2):
            output.append(nums[i+1])
            output.append(nums[i])
        return output