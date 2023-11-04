class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, max_one = 0, 0
        for x in nums:
            if x == 0: count = 0
            else:
                count += 1
                max_one = max(count, max_one)
        return max_one
