#https://leetcode.com/problems/max-consecutive-ones/
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                count = 0
            max_ones = max(max_ones, count)
        return max_ones
        