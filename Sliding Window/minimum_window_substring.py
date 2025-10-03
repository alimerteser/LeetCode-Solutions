from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqt = defaultdict(int)
        freqs = defaultdict(int)
        missing = len(t)
        l = 0
        res = ""

        for ch in t:
            freqt[ch] += 1

        for r in range(len(s)):
            freqs[s[r]] += 1
            if freqt[s[r]] > 0 and freqs[s[r]] <= freqt[s[r]]:
                missing -= 1
            while missing == 0:
                if res == "" or r - l + 1 < len(res):
                    res = s[l:r + 1]
                freqs[s[l]] -= 1
                if s[l] in t and freqs[s[l]] < freqt[s[l]]:
                    missing += 1
                l += 1

        return res
