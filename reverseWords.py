class Solution:
    def reverseWords(self, s: str) -> str:
        re = []
        for word in s.split():
            re.append(word[::-1])
        return ' '.join(re)

if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseWords('asd abc'))