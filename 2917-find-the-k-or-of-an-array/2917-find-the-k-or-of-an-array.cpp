class Solution {
public:
    int findKOr(vector<int>& nums, int k) {
        vector<int> dp(31, 0);

        for (int num : nums) {
            int i = 0;
            while (num > 0) {
                if (num & 1) dp[i] += 1;
                i += 1;
                num = num >> 1;
            }
        }
        int ans = 0;
        for (int i = 0; i < 31; ++i) {
            if (dp[i] >= k) ans |= (1 << i);
        }
        return ans;
    }
};