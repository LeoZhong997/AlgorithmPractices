from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            num = numbers[i] + numbers[j]
            if num == target:
                return [i + 1, j + 1]
            if num < target:
                i += 1
            else:
                j -= 1

     