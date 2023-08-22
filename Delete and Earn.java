class Solution {
    public int deleteAndEarn(int[] nums) {
        int max = 0;
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            max = Math.max(max, nums[i]);
        }
        int[] dp = new int[max+1];
        for (int i = 0; i < n; i++) {
            dp[nums[i]] += nums[i];
        }
        dp[1] = Math.max(dp[0], dp[1]);
        for (int i = 2; i < dp.length; i++) {
            dp[i] = Math.max(dp[i-1], dp[i-2]+dp[i]);
        }
        return dp[max];
    }
}
