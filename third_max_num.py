#https://leetcode.com/problems/third-maximum-number/
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        set_arr = set(nums)
        sort_arr = sorted(set_arr, reverse=True)
        if len(sort_arr) < 3:
            return max(sort_arr)
        else:
            return sort_arr[2]
        