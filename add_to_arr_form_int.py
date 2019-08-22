#https://leetcode.com/problems/add-to-array-form-of-integer/
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        s = ""
        res = []
        for num in A:
            s += str(num)

        sum_num = int(s) + K
        res = [int(x) for x in str(sum_num)]
        return res