class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        str_map = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in str_map:
                str_map[key] = []
            str_map[key].append(s)
        ans = [[] for key in str_map]
        k = 0
        for key in str_map:
            for s in str_map[key]:
                ans[k].append(s)
            k += 1 
        return ans
