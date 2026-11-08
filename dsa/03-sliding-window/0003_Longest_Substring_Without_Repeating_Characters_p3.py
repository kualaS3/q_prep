class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        R = 0
        d = set()
        best = 0
        while R < len(s):
            if s[R] not in d:
                d.add(s[R])
                R += 1
                if len(d) > best:
                    best = len(d)
            else:
                while s[R] in d:
                    d.remove(s[L])
                    L += 1
        return best
