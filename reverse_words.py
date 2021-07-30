class Solution:
    def reverseWords_m1(self, s: str) -> str:
		"""
		Time: O(n)
		Space: O(n)
		"""
		# use inter API
        return ' '.join(reversed(s.split()))
	
    def trim_spaces(self, s: str) -> list:
        left, right = 0, len(s) - 1
        # remove space at the start of s
        while left <= right and s[left] == ' ':
            left += 1
        # remove space at the end of s
        while left <= right and s[right] == ' ':
            right -= 1
        # remove redundant space at the middle of s
        output = []
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':
                output.append(s[left])
            left += 1
        return output

    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1

    def reverse_each_word(self, l: list) -> None:
        n = len(l)
        start = end = 0
        while start < n:
            # loop to the end of a word
            while end < n and l[end] != ' ':
                end += 1
            # reverse word
            self.reverse(l, start, end - 1)
            # update start and end
            start = end + 1
            end += 1

    def reverseWords_m2(self, s: str) -> str:
		"""
		Time: O(n)
		Space: O(n)
		"""
		# use self API
        l = self.trim_spaces(s)
        # reverse stirng
        self.reverse(l, 0, len(l) - 1)
        # reverse each word
        self.reverse_each_word(l)

        return ''.join(l)
	
	def reverseWords_m3(self, s: str) -> str:
		"""
		Time: O(n)
		Space: O(n)
		"""
		# use deque
        left, right = 0, len(s) - 1
        # remove space from the start of s
        while left <= right and s[left] == ' ':
            left += 1
        # remove space from the end of s
        while left <= right and s[right] == ' ':
            right -= 1

        d, word = collections.deque(), []
        # push word in the head of queue
        while left <= right:
            if s[left] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        d.appendleft(''.join(word))

        return ' '.join(d)


