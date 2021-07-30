class Solution:
    """"
    Time: O(n)
    Space: O(1)
    """"
    def majorityElement(self, nums: List[int]) -> int:
        """
        Boyer-Moore 投票算法       
        """
        candidate = -1
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            else:
                if candidate == num:
                    count += 1
                else:
                    count -= 1
        count = 0
        for num in nums:
            if num == candidate:
                count += 1
        if count * 2 >= len(nums):
            return candidate
        else:
            return -1
