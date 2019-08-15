#https://leetcode.com/problems/first-bad-version/
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        h = n
        while l < h:
            mid = (l + h)//2
            if isBadVersion(mid) == True:
                h = mid
            if isBadVersion(mid) == False:
                l = mid + 1
        return l
            