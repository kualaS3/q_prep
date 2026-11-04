# Time complexity = O(log n)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            i = (r + l) // 2
            curr = nums[i]

            if curr == target:
                return i
            if curr < target:
                l = i + 1
                continue
            if curr > target:
                r = i - 1
                continue

        return -1
