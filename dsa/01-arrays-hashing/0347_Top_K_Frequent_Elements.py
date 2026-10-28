class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for n in nums:
            d[n] = d.get(n,0) + 1 ### Remb shorthand for initialising and/or ++ to count
        ans = []
        for _ in range(k):
            key = max(d, key = d.get) ### argmax method for max()
            ans.append(key)
            del d[key]
        return ans
