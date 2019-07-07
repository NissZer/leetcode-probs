#link: https://leetcode.com/problems/squares-of-a-sorted-array/
class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        new_arr = []
        for num in A:
            n = num ** 2
            new_arr.append(n)
            
        sorted_arr = sorted(new_arr)
        return sorted_arr
