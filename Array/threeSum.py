from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time Complexity: O(N^2)
        # Space Complexity: O(N)
        n = len(nums)
        nums.sort()     # sort list
        ans = list()

        # first, enumerate val a
        for first in range(n):
            # must different from last a
            if first > 0 and nums[first - 1] == nums[first]:
                continue

            # init c idx at the end of list
            third = n - 1
            target = -nums[first]

            # second, enumerate val b
            for second in range(first + 1, n):
                # must different from last b
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue

                # change c idx, meanwhile, make sure b idx is on the left of c idx
                while second < third and nums[second] + nums[third] > target:
                    third -= 1

                # if b idx == c idx, even if b idx increase, it will not satisfy a+b+c=0, 
                # quit second for loop
                if second == third:
                    break

                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        return ans
