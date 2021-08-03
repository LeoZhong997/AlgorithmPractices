from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        slow = 0
        sum_nums = 0
        n = len(nums)
        min_len = n + 1
        for fast in range(n):
            sum_nums += nums[fast]
            if sum_nums >= target:
                while slow < fast:
                    if sum_nums - nums[slow] >= target:
                        sum_nums -= nums[slow]
                        slow += 1
                    else:
                        break
                min_len = min(min_len, fast - slow + 1)
        return min_len if min_len != n + 1 else 0

if __name__ == '__main__':
    sol = Solution()
    print(sol.minSubArrayLen(7, [2,3,1,2,4,3]))