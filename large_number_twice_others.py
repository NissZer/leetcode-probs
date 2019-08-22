#https://leetcode.com/problems/largest-number-at-least-twice-of-others/
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = max(nums)
        if all(max_num >= 2* num for num in nums if max_num != num):
            return nums.index(max_num)
        return -1
        