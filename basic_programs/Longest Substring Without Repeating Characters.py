class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = start = 0
        n = {}
        for end, char in enumerate(s):
            if n.get(char, -1) >= start:
                start = n[char] + 1
            max_len = max(max_len, end - start + 1)
            n[char] = end
        return max_len
