# Time complexity = O(log n)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            i = (l + r) // 2
            curr = nums[i]

            if curr < target:
                l = i + 1
            if curr > target:
                r = i - 1
            if curr == target:
                return i

        return l
