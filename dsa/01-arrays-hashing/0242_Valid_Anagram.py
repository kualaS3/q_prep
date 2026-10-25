class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        smap = {}
        for char in s:
            if char not in smap:
                smap[char] = 1
            else: 
                smap[char] += 1
        for char in t:
            if char not in smap:
                return False
            else:
                smap[char] -= 1
                if smap[char] == 0:
                    del smap[char]
        return len(smap) == 0 
