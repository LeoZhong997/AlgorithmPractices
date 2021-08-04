from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex += 1   # [1, ...]
        if rowIndex == 1:
            return [1]
        if rowIndex == 2:
            return [1, 1]
        re = [0] * rowIndex
        re[0] = re[1] = 1
        for i in range(3, rowIndex + 1):
            re[i - 1] = 1
            for j in range(i - 2, 0, -1):   # reverse travesal
                re[j] = re[j] + re[j - 1]
        return re