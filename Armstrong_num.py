#https://leetcode.com/problems/armstrong-number/
class Solution:
    def isArmstrong(self, N: int) -> bool:
        k = len(str(N))
        sum_n = 0
        for digit in str(N):
            sum_n += pow(int(digit), k)
        return sum_n == N

        