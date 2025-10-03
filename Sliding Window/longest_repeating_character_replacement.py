from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = defaultdict(int)
        l = 0
        longest = 0

        for r in range(len(s)):
            freqs[s[r]] += 1
            max_freq = max(list(freqs.values()))
            t = r - l + 1 - max_freq
            if t > k:
                freqs[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)

        return longest
