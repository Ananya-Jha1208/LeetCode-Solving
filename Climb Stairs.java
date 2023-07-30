class Solution {
    public int climbStairs(int n) {
        int st[] = new int[n+1];
        st[0] = 1;
        st[1] = 1;
        for (int i = 2; i <= n; i++) {
            st[i] = st[i-1] + st[i-2];
        }
        return st[n];
    }
}
