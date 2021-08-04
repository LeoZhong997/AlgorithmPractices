from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        re = [[1], [1, 1]]
        for i in range(3, numRows + 1):
            te = [0] * i
            te[0] = te[-1] = 1
            for j in range(1, i - 1):
                te[j] = re[-1][j-1] + re[-1][j]
            re.append(te)
        return re

            