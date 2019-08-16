#https://leetcode.com/problems/find-pivot-index/
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_nums = sum(nums) 
        left = 0
        #right = sum_nums - left - num
        for i, num in enumerate(nums):
            if left == (sum_nums - left - num):
                return i
            left += num
        return -1