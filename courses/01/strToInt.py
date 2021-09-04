class Solution:
    def strToInt(self, str: str) -> int:
        str = str.strip() # remove space
        if not str:
            return 0 # empty str
        
        res, i, sign = 0, 1, 1 # result, index for jointing, sign
        int_max, int_min, bndry = 2 ** 31 - 1, -2 ** 31, 2 ** 31 // 10 # record fixed val
        if str[0] == '-':
            sign = -1 # save sign
        elif str[0] != '+':
            i = 0 # joint num from first word
            
        for c in str[i:]:
            if not '0' <= c <= '9':
                break # non-number, break
            if res > bndry or (res == bndry and c > '7'): # key point!!!!!!
                return int_max if sign == 1 else int_min # number boundary check
            res = 10 * res + ord(c) - ord('0') # joint number
        return sign * res # add sign


    def strToIntV1(self, str: str) -> int:
        res, i, sign, length = 0, 0, 1, len(str) # result, index, sign
        int_max, int_min, bndry = 2 ** 31 - 1, -2 ** 31, 2 ** 31 // 10 # record fixed val
        
        if not str:
            return 0 # empty str
        while str[i] == ' ':
            i += 1
            if i == length:
                return 0 # str is all of 0
        if str[i] == '-':
            sign = -1
        if str[i] in '+-':
            i += 1
            
        for j in range(i, length):
            if not '0' <= str[j] <= '9':
                break # non-number, break
            if res > bndry or (res == bndry and str[j] > '7'): # key point!!!!!!
                return int_max if sign == 1 else int_min # number boundary check
            res = 10 * res + ord(str[j]) - ord('0') # joint number
        return sign * res # add sign

