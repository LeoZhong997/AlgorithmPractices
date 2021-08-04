from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        从左到右循环，记录最大值为 max，若 nums[i] < max, 则表明位置 i 需要调整, 
        循环结束，记录需要调整的最大位置 i 为 high; 
        同理，从右到左循环，记录最小值为 min, 若 nums[i] > min, 则表明位置 i 需要调整，
        循环结束，记录需要调整的最小位置 i 为 low.
        """
        n = len(nums)
        maxn, right = float('-inf'), -1     # max val in nums
        minn, left = float('inf'), -1       # min val in nums

        for i in range(n):
            if maxn > nums[i]:
                right = i
            else:
                maxn = nums[i]      # update max val 

            if minn < nums[n - i - 1]:  # reverse
                left = n - i - 1
            else:
                minn = nums[n - i - 1]  # update min val

        return 0 if right == -1 else right - left + 1