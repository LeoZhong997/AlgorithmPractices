from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sum_ = 0
        max_length = 0
        for fast in range(len(nums)):
            if nums[fast] == 0 and sum_ != 0:
                max_length = max(max_length, sum_)
                sum_ = 0
            if nums[fast] == 1:
                sum_ += 1
        return max(max_length, sum_)
