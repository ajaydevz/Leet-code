class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = copy.deepcopy(nums)
        q = deque()
        q.append(0)
        for i in range(1,len(nums)):
            while(q[-1] < i-k ):
                q.pop()
            dp[i] = max(dp[i],dp[q[-1]]+nums[i])
            while( len(q)>0 and dp[q[0]] <= dp[i] ):
                q.popleft()
            q.appendleft(i)
        return max(dp)