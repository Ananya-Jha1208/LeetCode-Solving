class Solution {
    public int maximumWealth(int[][] accounts) {
        // person is row
        // account is col
        int maxSum = 0;
        for (int person = 0; person < accounts.length; person++) {
            int wealthSum = 0;
            for (int account = 0; account < accounts[person].length; account++) {
                 // when starting new col, add it to sum of row
                  wealthSum += accounts[person][account];
            }
            if (wealthSum > maxSum) {
                maxSum = wealthSum;
            }
        }
        return maxSum;
    }
}
