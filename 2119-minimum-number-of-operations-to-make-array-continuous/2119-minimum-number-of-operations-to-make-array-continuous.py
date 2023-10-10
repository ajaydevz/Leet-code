class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        arr = sorted(set(nums))

        j = 0
        for item in arr:
            j += item - arr[j] > n-1

        return j + n - len(arr)