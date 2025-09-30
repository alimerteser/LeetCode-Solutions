from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l, r = 0, len(s1)-1
        freqs1 = defaultdict(int) #the string we are looking for
        freqs2 = defaultdict(int) #the string we are looking at

        for ch in s1:
            freqs1[ch] += 1

        for i in range(len(s1)):
            freqs2[s2[i]] += 1

        while r < len(s2):
            if freqs2 == freqs1:
                return True
            freqs2[s2[l]] -= 1
            if freqs2.get(s2[l]) <= 0:
                freqs2.pop(s2[l])
            l += 1
            r += 1
            if r < len(s2):
                freqs2[s2[r]] += 1

        return False