class Solution:
	"""
	Time: O(n)
	Space: (n)
	"""
    def reverseWords(self, s: str) -> str:
		# use inter API
        return ' '.join(reversed(s.split()))
