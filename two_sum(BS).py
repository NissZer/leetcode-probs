#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            l = i + 1
            h = len(numbers) - 1
            num2 = target - numbers[i]
            while l <= h:
                mid = (l+h)//2
                if numbers[mid] == num2:
                    return (i+1, mid+1)
                elif num2 < numbers[mid]:
                    h = mid - 1
                else:
                    l = mid + 1 