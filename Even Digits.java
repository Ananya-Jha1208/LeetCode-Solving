class Solution {
    public int findNumbers(int[] nums) {
        int count = 0;
        for (int num : nums) {
            if (even(num)) {
                count++;
            }
        }
        return count;
    }

    static boolean even(int num) {
        int numOfDig = digits2(num);
        return numOfDig % 2 == 0;
    }

    static int digits2(int num) {

        if (num < 0) {
            num = num * -1;
        }

        if (num == 0) {
            return 1;
        }

        return (int)(Math.log10(num)) + 1;
    }
}
