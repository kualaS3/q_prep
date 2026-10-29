class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        high_count = 0
        i = 0
        while i < len(s):
            curr = s[i]
            length = 1

            j = i+1
            seen = set()
            while j < len(s):
                if curr == s[j] or s[j] in seen:
                    break
                else: 
                    length += 1
                    seen.add(s[j])
                j += 1
            if high_count < length:
                high_count = length
            i += 1
        return high_count
